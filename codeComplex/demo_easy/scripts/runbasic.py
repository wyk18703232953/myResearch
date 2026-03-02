import time
import json
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
import os
import sys
import warnings
import traceback

warnings.filterwarnings("ignore")

import config

def constant(n, a, b):
    return a * np.ones_like(n) + b

def linear(n, a, b):
    return a * n + b

def quadratic(n, a, b, c):
    return a * n**2 + c

def cubic(n, a, b, c, d):
    return a * n**3 + d

def logarithmic(n, a, b):
    n_safe = np.maximum(n, 1e-10)
    return a * np.log(n_safe) + b

def n_log_n(n, a, b):
    n_safe = np.maximum(n, 1e-10)
    return a * n * np.log(n_safe) + b

MODELS = {
    "Constant": constant,
    "Linear": linear,
    "Quadratic": quadratic,
    "Cubic": cubic,
    "Logarithmic": logarithmic,
    "N Log N": n_log_n,
}

import timeit

def run_with_timeout(code_str, timeout_seconds):
    import signal
    import re
    import io
    
    def timeout_handler(signum, frame):
        raise TimeoutError(f"Execution timed out after {timeout_seconds} seconds")
    
    # 保存原始的 sys 模块和标准流
    import sys
    original_sys = sys
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    
    try:
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout_seconds)
        
        # 1. 解析代码字符串，分离代码内容和main函数调用
        parts = code_str.split('\n\nmain(')
        if len(parts) != 2:
            raise Exception("Invalid code format: expected 'code_content\n\nmain(n)'")
        
        code_content = parts[0]
        main_call = parts[1].rstrip(')')
        
        # 2. 提取n值
        try:
            n_value = eval(main_call)
        except:
            raise Exception(f"Invalid main call: main({main_call})")
        
        # 3. 准备环境 (Context) - 创建完全隔离的环境
        global_scope = {}
        
        # 4. 创建一个完全隔离的 sys 模块
        import types
        fake_sys = types.ModuleType('sys')
        
        # 复制原始 sys 的属性，但替换标准流
        fake_sys.__dict__.update(original_sys.__dict__)
        
        # 创建内存中的文件对象作为标准输入输出
        fake_stdin = io.StringIO()
        fake_stdout = io.StringIO()
        fake_stderr = io.StringIO()
        
        fake_sys.stdin = fake_stdin
        fake_sys.stdout = fake_stdout
        fake_sys.stderr = fake_stderr
        
        # 为 fake_stdout 和 fake_stderr 添加 encoding 属性（使用属性描述符）
        # 因为 io.StringIO 的 encoding 属性是只读的，我们需要用另一种方式
        class EncodingWrapper:
            def __init__(self, io_obj):
                self.io_obj = io_obj
            def write(self, text):
                if isinstance(text, str):
                    try:
                        return self.io_obj.write(text)
                    except UnicodeEncodeError:
                        return self.io_obj.write(text.encode('utf-8', 'replace').decode('utf-8'))
                return self.io_obj.write(str(text))
            def flush(self):
                pass
            def getvalue(self):
                return self.io_obj.getvalue()
            @property
            def encoding(self):
                return 'utf-8'
        
        # 包装标准流
        fake_sys.stdout = EncodingWrapper(fake_stdout)
        fake_sys.stderr = EncodingWrapper(fake_stderr)
        
        # 注意：EncodingWrapper 已经处理了安全的写入和刷新方法
        
        # 将 fake_sys 注入到 global_scope
        global_scope['sys'] = fake_sys
        
        # 5. 在计时前，先执行一次定义 (Compile & Define)
        # 这样 main 函数就被加载到了 global_scope 字典里，而且只做了一次
        exec(code_content, global_scope)
        
        # 6. 从字典里把函数捞出来
        if 'main' not in global_scope:
            raise Exception("main function not found in code")
        main_func = global_scope['main']
        import gc
        # 1. 强制垃圾回收，清空之前的残留
        gc.collect()
    
        # 2. 暂时关闭 GC，防止测试过程中 GC 启动干扰计时
        # 注意：如果你的算法本身极度依赖 GC 释放内存否则会 OOM，则不能关
        gc.disable()

        # 7. 【关键】直接测这个函数对象，没有任何 exec 开销
        # 注意：这里直接调用 main_func(n_value)，纯净无噪声
        times = timeit.repeat(stmt=lambda: main_func(n_value), repeat=5, number=1)
        min_time = np.min(times)  # 计算最小执行时间（秒）
        
        signal.alarm(0)
        gc.enable()
        return (True, min_time, None)
        
    except TimeoutError as e:
        signal.alarm(0)
        return (False, 0, str(e))
    except Exception as e:
        signal.alarm(0)
        return (False, 0, str(e))
    finally:
        # 确保恢复原始的 sys.stdout 和 sys.stderr
        try:
            sys.stdout = original_stdout
            sys.stderr = original_stderr
        except:
            # 如果恢复失败，至少确保有基本的 stdout/stderr
            import io
            sys.stdout = io.StringIO()
            sys.stderr = io.StringIO()

def clean_data(x_raw, y_raw):
    if len(x_raw) < 4:
        return x_raw, y_raw

    mask_cold_start = np.ones(len(x_raw), dtype=bool)
    if y_raw[0] > y_raw[1]:
        mask_cold_start[0] = False
    
    x_clean = x_raw[mask_cold_start]
    y_clean = y_raw[mask_cold_start]

    if len(x_clean) > 5:
        try:
            coeffs = np.polyfit(x_clean, y_clean, 2)
            p = np.poly1d(coeffs)
            y_pred_trend = p(x_clean)
            
            residuals = y_clean - y_pred_trend
            mean_res = np.mean(residuals)
            std_res = np.std(residuals)
            
            if std_res > 1e-6:
                z_scores = np.abs((residuals - mean_res) / std_res)
                mask_z = z_scores < 2.5
                
                if np.sum(mask_z) >= 4:
                    outliers_count = len(x_clean) - np.sum(mask_z)
                    if outliers_count > 0:
                        x_clean = x_clean[mask_z]
                        y_clean = y_clean[mask_z]
        except Exception as e:
            pass

    return x_clean, y_clean

def process_code_file(code_path, expected_models, base_dir):
    if not os.path.exists(code_path):
        print(f"错误：文件 {code_path} 不存在")
        return False
    
    file_name = os.path.basename(code_path)
    base_name = os.path.splitext(file_name)[0]
    result_dir = os.path.join(base_dir, f"results_{base_name}")
    os.makedirs(result_dir, exist_ok=True)
    
    with open(code_path, 'r', encoding='utf-8') as f:
        code_content = f.read()

    test_results = []
    
    temp_results_path = os.path.join(result_dir, "temp_results.npz")
    start_n = config.start_n
    
    if os.path.exists(temp_results_path):
        try:
            loaded = np.load(temp_results_path)
            if 'results' in loaded:
                test_results = loaded['results'].tolist()
            else:
                test_results = loaded[loaded.files[0]].tolist()
            if test_results:
                start_n = int(test_results[-1][0]) + config.step
                print(f"恢复进度：从 n={start_n} 继续")
        except Exception:
            pass

    print(f"开始测试 {file_name}: n={start_n} -> {config.max_n}")

    REPEAT_COUNT = 3
    TIMEOUT_SECONDS = 1

    if len(test_results) == 0:
        print("   [系统] 正在进行预热 (Warm-up)...")
        try:
            warmup_code = f"{code_content}\n\nmain({start_n})"
            success, exec_time, error = run_with_timeout(warmup_code, TIMEOUT_SECONDS)
            if not success:
                print(f"   [警告] 预热失败: {error}")
        except Exception as e:
            print(f"   [警告] 预热失败: {e}")

    try:
        # for n in range(start_n, config.max_n + 1, config.step):
        k = max(1, (start_n + 1).bit_length() - 1) # 让 (2^k - 1) >= start_n
        while True:
            n = (1 << k) - 1
            if n > config.max_n:
                break
        # for n in range(start_n, config.max_n + 1, config.step):
    
            # print('n=',n)
            run_code = f"{code_content}\n\nmain({n})"
            
            run_times = []
            for attempt in range(REPEAT_COUNT):
                success, exec_time, error = run_with_timeout(run_code, TIMEOUT_SECONDS)
                
                if success:
                    run_times.append(exec_time * 1000)
                    # print(f"   [成功] n={n}, 第{attempt+1}次运行成功，耗时 {exec_time*1000:.4f} ms")
                else:
                    print(f"   [警告] n={n}, 第{attempt+1}次运行失败: {error}")
                    if "Timeout" in error:
                        print(f"   [停止] n={n} 超时，停止测试")
                        break
                    continue
            
            if len(run_times) == 0:
                print(f"   [错误] n={n} 所有运行都失败，跳过")
                break
            # median_time = np.median(run_times)
            # test_results.append((n, median_time))
            min_time = np.min(run_times)
            # print(f"   [成功] n={n}, 最小耗时 {min_time:.4f} ms")
            test_results.append((n, min_time))
            
            if len(test_results) % 10 == 0:
                np.savez(temp_results_path, results=test_results)
            k+=1
                
    except KeyboardInterrupt:
        print("\n用户中断测试...")
    finally:
        final_data_path = os.path.join(result_dir, "time_results.npz")
        np.savez(final_data_path, results=test_results)

    if len(test_results) < 5:
        print("数据点不足 (<5)，跳过拟合分析")
        return False

    data_arr = np.array(test_results)
    x_raw = data_arr[:, 0]
    y_raw = data_arr[:, 1]
    
    idx = np.argsort(x_raw)
    x_raw = x_raw[idx]
    y_raw = y_raw[idx]

    x_data, y_data = clean_data(x_raw, y_raw)

    if len(x_data) < 4:
        print("   [警告] 清洗后数据过少，回退使用原始数据。")
        x_data, y_data = x_raw, y_raw

    fit_report = {}
    best_model_name = "None"
    
    is_constant, constant_score = detect_constant_by_variation(x_data, y_data)
    is_logarithmic, logarithmic_score, logarithmic_feature_count = detect_logarithmic_by_variation(x_data, y_data)
    is_nlogn, nlogn_score, nlogn_feature_count = detect_nlogn_by_variation(x_data, y_data)
    
    if is_constant:
        print(f"   [检测] 检测到常数复杂度特征 (confidence={constant_score:.2f})")
    
    if is_logarithmic:
        print(f"   [检测] 检测到对数复杂度特征 (score={logarithmic_score:.2f}, features={logarithmic_feature_count})")
    
    if is_nlogn:
        print(f"   [检测] 检测到nlogn复杂度特征 (score={nlogn_score:.2f}, features={nlogn_feature_count})")
    
    print("正在拟合模型...")
    
    for name, func in MODELS.items():
        try:
            popt, pcov = curve_fit(func, x_data, y_data, maxfev=10000)
            y_pred = func(x_data, *popt)
            
            if name == "Constant":
                pred_mean = np.mean(y_pred)
                ss_res = np.sum((y_data - pred_mean) ** 2)
                ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)
                r2 = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
                
                y_mean = np.mean(y_data)
                y_std = np.std(y_data)
                relative_std = y_std / (y_mean + 1e-10)
                
                if relative_std < 0.03:
                    r2 = 0.95
                elif relative_std < 0.05:
                    r2 = 0.90
                elif relative_std < 0.08:
                    r2 = 0.85
                else:
                    r2 = max(r2, 0.70)
            else:
                r2 = r2_score(y_data, y_pred)
            
            resid = y_data - y_pred
            ssr = np.sum(resid**2)
            if ssr <= 0: ssr = 1e-10
            k = len(popt)
            n_samples = len(y_data)
            
            aic = 2 * k + n_samples * np.log(ssr / n_samples)
            bic = n_samples * np.log(ssr / n_samples) + k * np.log(n_samples)
            
            fit_report[name] = {
                "r2": r2,
                "aic": aic,
                "bic": bic,
                "params": popt.tolist()
            }
                
        except Exception as e:
            fit_report[name] = {"r2": -np.inf, "success": False}
    
    valid_bics = [
        info.get("bic", np.inf)
        for info in fit_report.values()
        if np.isfinite(info.get("bic", np.inf))
    ]
    bic_min = min(valid_bics) if valid_bics else None
    n_samples = len(y_data)
    best_conf_score = -np.inf
    
    for name, info in fit_report.items():
        r2 = info.get("r2", -np.inf)
        bic = info.get("bic", np.inf)
        
        if not (np.isfinite(r2) and np.isfinite(bic) and bic_min is not None):
            info["confidence_score"] = -np.inf
            continue
        
        r2_clamped = min(max(r2, 0.0), 1.0)
        bic_gap = bic - bic_min
        bic_weight = math.exp(-0.5 * bic_gap)
        
        if name == "Constant":
            complexity_penalty = 0
            if is_constant:
                r2_clamped = min(r2_clamped + 0.4, 1.0)
            # 如果检测到logarithmic或nlogn，大幅降低constant分数
            if is_logarithmic or is_nlogn:
                r2_clamped = max(r2_clamped - 0.5, 0.0)
        elif name == "Logarithmic":
            complexity_penalty = 0.002  # 极低的惩罚
            # 使用logarithmic_score
            if logarithmic_score > 0.6:
                r2_clamped = min(r2_clamped + 0.5, 1.0)
            elif logarithmic_score > 0.4:
                r2_clamped = min(r2_clamped + 0.4, 1.0)
            elif logarithmic_score > 0.2:
                r2_clamped = min(r2_clamped + 0.3, 1.0)
            # 如果检测到constant，大幅降低logarithmic分数
            if is_constant:
                r2_clamped = max(r2_clamped - 0.3, 0.0)
            # 如果检测到nlogn，降低logarithmic分数
            if is_nlogn:
                r2_clamped = max(r2_clamped - 0.1, 0.0)
        elif name == "N Log N":
            complexity_penalty = 0.002  # 极低的惩罚
            # 使用nlogn_score
            if nlogn_score > 0.6:
                r2_clamped = min(r2_clamped + 0.5, 1.0)
            elif nlogn_score > 0.4:
                r2_clamped = min(r2_clamped + 0.4, 1.0)
            elif nlogn_score > 0.2:
                r2_clamped = min(r2_clamped + 0.3, 1.0)
            # 如果检测到constant，大幅降低nlogn分数
            if is_constant:
                r2_clamped = max(r2_clamped - 0.3, 0.0)
        elif name == "Linear":
            complexity_penalty = 0.01
            # 如果检测到constant，大幅降低linear分数
            if is_constant:
                r2_clamped = max(r2_clamped - 0.4, 0.0)
            # 如果检测到logarithmic，降低linear分数
            if is_logarithmic:
                r2_clamped = max(r2_clamped - 0.15, 0.0)
            # 如果检测到nlogn，降低linear分数
            if is_nlogn:
                r2_clamped = max(r2_clamped - 0.15, 0.0)
        else:
            complexity_penalty = 0.02
        
        if name == "Constant":
            confidence_score = 0.5 * r2_clamped + 0.3 * bic_weight + 0.2 * constant_score - complexity_penalty
        elif name == "Logarithmic":
            confidence_score = 0.5 * r2_clamped + 0.3 * bic_weight + 0.2 * logarithmic_score - complexity_penalty
        elif name == "N Log N":
            confidence_score = 0.5 * r2_clamped + 0.3 * bic_weight + 0.2 * nlogn_score - complexity_penalty
        else:
            confidence_score = 0.6 * r2_clamped + 0.4 * bic_weight - complexity_penalty
        
        confidence_score = min(max(confidence_score, 0.0), 1.0)
        info["confidence_score"] = confidence_score
        
        if confidence_score > best_conf_score:
            best_conf_score = confidence_score
            best_model_name = name
    
    print(f"分析完成。最佳拟合模型: {best_model_name} (Confidence={best_conf_score:.4f})")
    
    plt.figure(figsize=(12, 7))
    
    mask_kept = np.isin(x_raw, x_data) & np.isin(y_raw, y_data)
    
    if not np.all(mask_kept):
        x_rejected = x_raw[~mask_kept]
        y_rejected = y_raw[~mask_kept]
        plt.scatter(x_rejected, y_rejected, color='gray', marker='x', s=50, alpha=0.5, label='Outliers (Ignored)')

    plt.scatter(x_data, y_data, color='blue', alpha=0.6, label='Valid Data')
    
    if best_model_name in fit_report:
        best_info = fit_report[best_model_name]
        x_smooth = np.linspace(min(x_raw), max(x_raw), 500)
        y_smooth = MODELS[best_model_name](x_smooth, *best_info['params'])
        
        plt.plot(x_smooth, y_smooth, 'r-', linewidth=2, 
                 label=f'Best Fit: {best_model_name} ($R^2={best_info["r2"]:.3f}$)')
        
    plt.title(f"Time Complexity: {file_name}\n(Raw data count: {len(x_raw)}, Cleaned: {len(x_data)})")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(result_dir, "best_fit.png"))
    plt.close()
    
    with open(os.path.join(result_dir, "analysis_report.json"), 'w') as f:
        report_with_metadata = {
            "valid_points": len(x_data),
            "models": fit_report
        }
        json.dump(report_with_metadata, f, indent=2)

    is_success = False
    if best_model_name != "None":
        aliases = {
            'Logarithmic': ['logn', 'logarithmic', 'log'],
            'Linear': ['linear', 'o(n)'],
            'Quadratic': ['quadratic', 'o(n^2)'],
            'Cubic': ['cubic', 'o(n^3)'],
            'N Log N': ['nlogn', 'n_log_n']
        }
        
        cleaned_best = best_model_name
        for expected in expected_models:
            expected_lower = expected.lower()
            if expected_lower == cleaned_best.lower():
                is_success = True
                break
            if cleaned_best in aliases:
                if expected_lower in aliases[cleaned_best]:
                    is_success = True
                    break
                    
    return is_success

def main():
    global_stats = {
        'total': 0, 'success': 0, 'failed': 0, 
        'failed_files': []
    }
    
    folder_config = {
        'quadratic': (config.quadratic_folder_path, ['Quadratic']),
        'cubic': (config.cubic_folder_path, ['Cubic']),
        'constant': (config.constant_folder_path, ['Constant', 'constant']),
        'logn': (config.logn_folder_path, ['Logarithmic', 'logn']),
        'linear': (config.linear_folder_path, ['Linear']),
        'nlogn': (config.nlogn_folder_path, ['N Log N', 'nlogn', 'n_log_n']),
        'np': (config.np_folder_path, ['NP']),
    }
    
    base_dir_map = {
        'constant': config.constant_results_base_dir,
        'logn': config.logn_results_base_dir,
        'linear': config.linear_results_base_dir,
        'nlogn': config.nlogn_results_base_dir,
        'quadratic': config.quadratic_results_base_dir,
        'cubic': config.cubic_results_base_dir,
        'np': config.np_results_base_dir,
    }
    
    for folder_type in folder_config:
        print(f"\n{'='*60}")
        print(f"正在处理类型: {folder_type}")
        print(f"{'='*60}")
        
        folder_path, expected_models = folder_config[folder_type]

        if not os.path.exists(folder_path):
            print(f"文件夹不存在: {folder_path}")
            continue
            
        python_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.py')])
        total_files = min(len(python_files), 1000)
        python_files = python_files[:total_files]
        
        type_stats = {
            'total': total_files, 'success': 0, 'failed': 0,
            'failed_files': []
        }
        
        print(f"找到 {total_files} 个文件，开始处理...")
                       
        base_dir = base_dir_map[folder_type]
                       
        for i, file_name in enumerate(python_files, 1):
            # if(i<540):
            #     continue
            full_path = os.path.join(folder_path, file_name)
            print(f"\n[{i}/{total_files}] 处理文件: {file_name}")
            # time.sleep(1)
            try:
                success = process_code_file(full_path, expected_models, base_dir)
                if success:
                    print(">>> 判定结果: 符合预期 ✅")
                    type_stats['success'] += 1
                    global_stats['success'] += 1
                else:
                    print(">>> 判定结果: 不符合预期 ❌")
                    type_stats['failed'] += 1
                    type_stats['failed_files'].append(file_name)
                    global_stats['failed'] += 1
                    global_stats['failed_files'].append(f"{folder_type}/{file_name}")
                    
            except Exception as e:
                print(f"处理发生未捕获异常: {e}")
                traceback.print_exc()
                type_stats['failed'] += 1
                global_stats['failed'] += 1
                type_stats['failed_files'].append(file_name)
                global_stats['failed_files'].append(f"{folder_type}/{file_name}")
                
        actual_processed = max(100, total_files)
        global_stats['total'] += actual_processed
        
        print(f"\n{'='*50}")
        print(f"类型 {folder_type} 统计报告")
        print(f"{'='*50}")
        print(f"总文件数: {type_stats['total']}")
        print(f"成功匹配: {type_stats['success']}")
        print(f"失败/不匹配: {type_stats['failed']}")
        if type_stats['failed_files']:
            print("\n失败文件列表:")
            for f in type_stats['failed_files'][:10]:
                print(f" - {f}")
                
        stats_path = os.path.join(base_dir, f"stats_{folder_type}.json")
        with open(stats_path, 'w') as f:
            json.dump(type_stats, f, indent=2)
        print(f"\n类型统计已保存至: {stats_path}")
            

    print("\n" + "="*50)
    print("最终统计报告")
    print("="*50)
    print(f"总文件数: {global_stats['total']}")
    print(f"成功匹配: {global_stats['success']}")
    print(f"失败/不匹配: {global_stats['failed']}")
    if global_stats['failed_files']:
        print("\n失败文件列表 (Top 10):")
        for f in global_stats['failed_files'][:10]:
            print(f" - {f}")
            
    global_stats_path = os.path.join(config.linear_results_base_dir, "stats_global.json")
    with open(global_stats_path, 'w') as f:
        json.dump(global_stats, f, indent=2)
    print(f"\n全局统计已保存至: {global_stats_path}")

if __name__ == "__main__":
    main()