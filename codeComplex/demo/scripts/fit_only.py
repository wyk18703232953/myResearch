import time
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
import os
import sys
import warnings
import traceback

# 忽略拟合过程中的 RuntimeWarning
warnings.filterwarnings("ignore")

# 导入配置文件
import config

# ==========================================
# 1. 定义安全的复杂度模型函数
# ==========================================

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

# ==========================================
# 2. 新增：数据清洗与异常处理函数
# ==========================================

def run_with_timeout(code_str, timeout_seconds):
    """
    在指定超时时间内执行代码
    
    Args:
        code_str: 要执行的代码字符串
        timeout_seconds: 超时时间（秒）
    
    Returns:
        (success: bool, execution_time: float, error: str)
    """
    import signal
    
    def timeout_handler(signum, frame):
        raise TimeoutError(f"Execution timed out after {timeout_seconds} seconds")
    
    try:
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout_seconds)
        
        t0 = time.perf_counter()
        exec(code_str, {})
        t1 = time.perf_counter()
        
        signal.alarm(0)  # 取消定时器
        return (True, t1 - t0, None)
        
    except TimeoutError as e:
        signal.alarm(0)
        return (False, 0, str(e))
    except Exception as e:
        signal.alarm(0)
        return (False, 0, str(e))

def clean_data(x_raw, y_raw):
    """
    清洗数据：
    1. 剔除冷启动异常（如果第1个点显著大于第2个点，剔除）
    2. 基于残差剔除离群点 (Z-Score)
    """
    if len(x_raw) < 4:
        return x_raw, y_raw

    # --- 步骤 1: 冷启动检测 ---
    # 时间复杂度通常是单调递增的。如果 y[0] > y[1]，说明 n=1000 比 n=1100 还慢，
    # 这绝对是冷启动导致的异常。
    mask_cold_start = np.ones(len(x_raw), dtype=bool)
    if y_raw[0] > y_raw[1]:
        print(f"   [清洗] 检测到冷启动异常点 (n={x_raw[0]}, t={y_raw[0]:.2f}ms)，已剔除。")
        mask_cold_start[0] = False
    
    x_clean = x_raw[mask_cold_start]
    y_clean = y_raw[mask_cold_start]

    # --- 步骤 2: 统计学离群点剔除 (Z-Score) ---
    if len(x_clean) > 5:
        # 使用通用二次多项式拟合趋势（二次多项式能较好地兼容 Linear 到 Quadratic 的区间）
        # 这里只是为了找“大概趋势线”来计算残差
        try:
            coeffs = np.polyfit(x_clean, y_clean, 2)
            p = np.poly1d(coeffs)
            y_pred_trend = p(x_clean)
            
            # 计算残差
            residuals = y_clean - y_pred_trend
            mean_res = np.mean(residuals)
            std_res = np.std(residuals)
            
            # 如果标准差太小（数据非常完美），就不要剔除了，防止误杀
            if std_res > 1e-6:
                # 剔除超过 2.5 倍标准差的点
                z_scores = np.abs((residuals - mean_res) / std_res)
                mask_z = z_scores < 2.5
                
                # 如果剔除后剩下的点太少，就放弃这一步
                if np.sum(mask_z) >= 4:
                    outliers_count = len(x_clean) - np.sum(mask_z)
                    if outliers_count > 0:
                        print(f"   [清洗] 基于统计剔除了 {outliers_count} 个离群噪点。")
                        x_clean = x_clean[mask_z]
                        y_clean = y_clean[mask_z]
        except Exception as e:
            print(f"   [清洗] 统计清洗步骤失败，跳过: {e}")

    return x_clean, y_clean

# ==========================================
# 3. 核心处理函数
# ==========================================
def check_power_law_slope(x_data, y_data):
    """
    通过 Log-Log 线性拟合估算增长的幂次。
    slope ≈ 1.0 -> Linear
    slope ≈ 2.0 -> Quadratic
    slope ≈ 3.0 -> Cubic
    """
    try:
        # 过滤掉 <=0 的点避免 log 报错
        valid_mask = (x_data > 0) & (y_data > 0)
        if np.sum(valid_mask) < 4: return 0
        
        log_x = np.log(x_data[valid_mask])
        log_y = np.log(y_data[valid_mask])
        
        # 线性拟合 log(y) = b * log(x) + a，其中 b 是斜率
        coeffs = np.polyfit(log_x, log_y, 1)
        slope = coeffs[0]
        return slope
    except:
        return 0
        
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

    # --- 数据收集阶段 ---
    test_results = []
    
    # 检查断点续传
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

    # >>> 新增：配置参数 <<<
    REPEAT_COUNT = 3  # 每个n重复运行的次数 r
    TIMEOUT_SECONDS = 30  # 单次运行超时时间 τ (秒)

    # >>> 新增：预热 (Warm-up) <<<
    # 执行一次空跑，不计入结果，用于让 JIT 编译和缓存生效
    if len(test_results) == 0: # 只有刚开始跑才需要预热
        print("   [系统] 正在进行预热 (Warm-up)...")
        try:
            warmup_code = f"{code_content}\n\nmain({start_n})"
            success, exec_time, error = run_with_timeout(warmup_code, TIMEOUT_SECONDS)
            if not success:
                print(f"   [警告] 预热失败: {error}")
        except Exception as e:
            print(f"   [警告] 预热失败: {e}")

    try:
        for n in range(start_n, config.max_n + 1, config.step):
            run_code = f"{code_content}\n\nmain({n})"
            
            # >>> 新增：重复运行 r 次，取中位数 <<<
            run_times = []
            for attempt in range(REPEAT_COUNT):
                # print(f"   [运行] n={n}, 第{attempt+1}次运行...")
                success, exec_time, error = run_with_timeout(run_code, TIMEOUT_SECONDS)
                
                if success:
                    run_times.append(exec_time * 1000)  # 转换为毫秒
                    # print(f"   [成功] n={n}, 第{attempt+1}次运行耗时: {exec_time:.6f}s (转换为 {run_times[-1]:.3f}ms)")
                else:
                    print(f"   [警告] n={n}, 第{attempt+1}次运行失败: {error}")
                    if "Timeout" in error:
                        print(f"   [停止] n={n} 超时，停止测试")
                        break
                    continue
            
            if len(run_times) == 0:
                print(f"   [错误] n={n} 所有运行都失败，跳过")
                break
            
            # 取中位数作为代表值
            median_time = np.median(run_times)
            test_results.append((n, median_time))
            
            if len(test_results) % 10 == 0:
                np.savez(temp_results_path, results=test_results)
                
    except KeyboardInterrupt:
        print("\n用户中断测试...")
    finally:
        final_data_path = os.path.join(result_dir, "time_results.npz")
        np.savez(final_data_path, results=test_results)

    # --- 拟合分析阶段 ---
    if len(test_results) < 5:
        print("数据点不足 (<5)，跳过拟合分析")
        return False

    # 准备原始数据
    data_arr = np.array(test_results)
    x_raw = data_arr[:, 0]
    y_raw = data_arr[:, 1]
    
    # 排序
    idx = np.argsort(x_raw)
    x_raw = x_raw[idx]
    y_raw = y_raw[idx]

    # >>> 调用数据清洗 <<<
    x_data, y_data = clean_data(x_raw, y_raw)

    # 如果清洗后数据太少，回退到使用原始数据（虽然可能有噪声）
    if len(x_data) < 4:
        print("   [警告] 清洗后数据过少，回退使用原始数据。")
        x_data, y_data = x_raw, y_raw

    fit_report = {}
    best_score = -np.inf
    best_model_name = "None"
    
    print("正在拟合模型...")
    
    for name, func in MODELS.items():
        try:
            # 使用清洗后的数据进行拟合
            popt, pcov = curve_fit(func, x_data, y_data, maxfev=10000)
            y_pred = func(x_data, *popt)
            r2 = r2_score(y_data, y_pred)
            
            # 计算 AIC/BIC
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
            
            if r2 > best_score:
                best_score = r2
                best_model_name = name
                
        except Exception as e:
            fit_report[name] = {"r2": -np.inf, "success": False}

    print(f"分析完成。最佳拟合模型: {best_model_name} (R2={best_score:.4f})")
    
    # --- 绘图与报告保存 ---
    
    plt.figure(figsize=(12, 7)) # 稍微大一点
    
    # 1. 绘制被剔除的点（灰色叉叉）
    # 找出原始数据中不在清洗后数据里的点
    mask_kept = np.isin(x_raw, x_data) & np.isin(y_raw, y_data) 
    # 注意：这里简单的isin可能在y值完全相同时有误判，但对于浮点时间基本安全
    
    if not np.all(mask_kept):
        x_rejected = x_raw[~mask_kept]
        y_rejected = y_raw[~mask_kept]
        plt.scatter(x_rejected, y_rejected, color='gray', marker='x', s=50, alpha=0.5, label='Outliers (Ignored)')

    # 2. 绘制有效数据点（蓝色圆点）
    plt.scatter(x_data, y_data, color='blue', alpha=0.6, label='Valid Data')
    
    # 3. 绘制最佳拟合曲线
    if best_model_name in fit_report:
        best_info = fit_report[best_model_name]
        x_smooth = np.linspace(min(x_raw), max(x_raw), 500) # 画线覆盖全范围
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
        json.dump(fit_report, f, indent=2)

    # --- 结果判定 ---
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

# ==========================================
# 4. 主程序入口
# ==========================================

def main():
    global_stats = {
        'total': 0, 'success': 0, 'failed': 0, 
        'failed_files': []
    }
    
    folder_type = 'constant'  # 可在此处修改

    folder_config = {
        'constant': (config.constant_folder_path, ['Constant']),
        'logn': (config.logn_folder_path, ['Logarithmic', 'logn']),
        'linear': (config.linear_folder_path, ['Linear']),
        'quadratic': (config.quadratic_folder_path, ['Quadratic']),
        'cubic': (config.cubic_folder_path, ['Cubic']),
        'nlogn': (config.nlogn_folder_path, ['N Log N'])
    }
    
    if folder_type not in folder_config:
        print(f"未知的类型: {folder_type}")
        return
        
    folder_path, expected_models = folder_config[folder_type]

    if not os.path.exists(folder_path):
        print(f"文件夹不存在: {folder_path}")
        return
        
    python_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.py')])
    total_files = len(python_files)
    global_stats['total'] = total_files
    
    print(f"找到 {total_files} 个文件，开始处理...")
    
    base_dir_map = {
        'constant': config.constant_results_base_dir,
        'logn': config.logn_results_base_dir,
        'linear': config.linear_results_base_dir,
        'quadratic': config.quadratic_results_base_dir,
        'cubic': config.cubic_results_base_dir,
        'nlogn': config.nlogn_results_base_dir
    }
    base_dir = base_dir_map.get(folder_type, config.linear_results_base_dir)
                      
    for i, file_name in enumerate(python_files, 1):
        full_path = os.path.join(folder_path, file_name)
        print(f"\n[{i}/{total_files}] 处理文件: {file_name}")
        if(i>=1):
            try:
                success = process_code_file(full_path, expected_models, base_dir)
                if success:
                    print(">>> 判定结果: 符合预期 ✅")
                    global_stats['success'] += 1
                else:
                    print(">>> 判定结果: 不符合预期 ❌")
                    global_stats['failed'] += 1
                    global_stats['failed_files'].append(file_name)
                    
            except Exception as e:
                print(f"处理发生未捕获异常: {e}")
                global_stats['failed'] += 1
                global_stats['failed_files'].append(file_name)
            

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
            
    stats_path = os.path.join(base_dir, f"stats_{folder_type}.json")
    with open(stats_path, 'w') as f:
        json.dump(global_stats, f, indent=2)
    print(f"\n统计已保存至: {stats_path}")

if __name__ == "__main__":
    main()