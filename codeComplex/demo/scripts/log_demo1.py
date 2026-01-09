import time
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
import os
import sys
import warnings

# 忽略拟合过程中的 RuntimeWarning (如 log(0), overflow 等)
warnings.filterwarnings("ignore")

# 导入配置文件 (假设你本地有 config.py)
import config


# ==========================================
# 1. 定义安全的复杂度模型函数
# ==========================================

def constant(n, a, b):
    # O(1)
    return a * np.ones_like(n) + b

def linear(n, a, b):
    # O(n)
    return a * n + b

def quadratic(n, a, b, c):
    # O(n^2)
    return a * n**2 + c

def cubic(n, a, b, c, d):
    # O(n^3)
    return a * n**3 + d

def logarithmic(n, a, b):
    # O(log n) - 增加安全保护防止 log(0)
    n_safe = np.maximum(n, 1e-10)
    return a * np.log(n_safe) + b

def n_log_n(n, a, b):
    # O(n log n)
    n_safe = np.maximum(n, 1e-10)
    return a * n * np.log(n_safe) + b

def exponential(n, a, b):
    # O(2^n) - 增加裁剪防止溢出
    # 注意：指数增长极快，通常只能拟合非常小的 n
    val = np.clip(b * n, -100, 100) 
    return a * np.exp(val)

# 模型字典
MODELS = {
    "Constant": constant,
    "Linear": linear,
    "Quadratic": quadratic,
    "Cubic": cubic,
    "Logarithmic": logarithmic,
    "N Log N": n_log_n,
    # "Exponential": exponential, # 指数模型极其不稳定，通常建议在特定需求下开启
}

# ==========================================
# 2. 核心处理函数
# ==========================================

def process_code_file(code_path, expected_models, base_dir):
    """
    处理单个代码文件：执行代码 -> 收集数据 -> 拟合模型 -> 生成报告
    """
    if not os.path.exists(code_path):
        print(f"错误：文件 {code_path} 不存在")
        return False
    
    # --- 准备工作 ---
    file_name = os.path.basename(code_path)
    base_name = os.path.splitext(file_name)[0]
    result_dir = os.path.join(base_dir, f"results_{base_name}")
    os.makedirs(result_dir, exist_ok=True)
    
    # 读取代码
    with open(code_path, 'r', encoding='utf-8') as f:
        code_content = f.read()

    # --- 数据收集阶段 ---
    test_results = []
    
    # 检查是否有断点续传数据
    temp_results_path = os.path.join(result_dir, "temp_results.npz")
    start_n = config.start_n
    
    if os.path.exists(temp_results_path):
        try:
            loaded = np.load(temp_results_path)
            # 兼容处理：检查是 'results' 还是 'arr_0'
            if 'results' in loaded:
                test_results = loaded['results'].tolist()
            else:
                test_results = loaded[loaded.files[0]].tolist()
                
            if test_results:
                start_n = int(test_results[-1][0]) + config.step
                print(f"恢复进度：从 n={start_n} 继续")
        except Exception as e:
            print(f"读取临时文件失败，重新开始: {e}")

    print(f"开始测试 {file_name}: n={start_n} -> {config.max_n}")

    try:
        # 执行测试循环
        for n in range(start_n, config.max_n + 1, config.step):
            # 构造运行代码
            # 假设用户代码中定义了 main(n) 或类似入口
            run_code = f"{code_content}\n\nmain({n})"
            
            t0 = time.perf_counter()
            exec_globals = {}
            
            # 执行代码
            try:
                exec(run_code, exec_globals)
            except Exception as e:
                print(f"代码执行出错 (n={n}): {e}")
                break
                
            t1 = time.perf_counter()
            run_time_ms = (t1 - t0) * 1000
            test_results.append((n, run_time_ms))
            
            # 定期保存
            if len(test_results) % 10 == 0:
                np.savez(temp_results_path, results=test_results)
                
    except KeyboardInterrupt:
        print("\n用户中断测试，正在保存已收集数据...")
    finally:
        # 保存最终原始数据
        final_data_path = os.path.join(result_dir, "time_results.npz")
        np.savez(final_data_path, results=test_results)
        print(f"数据收集完成，共 {len(test_results)} 个数据点")

    # --- 拟合分析阶段 ---
    if len(test_results) < 5:
        print("数据点不足 (<5)，跳过拟合分析")
        return False

    # 准备数据
    data_arr = np.array(test_results)
    x_data = data_arr[:, 0]
    y_data = data_arr[:, 1]
    
    # 排序（以防万一）
    idx = np.argsort(x_data)
    x_data = x_data[idx]
    y_data = y_data[idx]

    fit_report = {}
    best_score = -np.inf
    best_model_name = "None"
    
    print("\n正在拟合模型...")
    
    # 遍历所有模型进行拟合
    for name, func in MODELS.items():
        try:
            # 1. 拟合
            # p0 可以根据需要添加，或者让 scipy 自动推断
            popt, pcov = curve_fit(func, x_data, y_data, maxfev=10000)
            
            # 2. 预测
            y_pred = func(x_data, *popt)
            
            # 3. 计算指标
            # R^2
            r2 = r2_score(y_data, y_pred)
            
            # AIC / BIC 计算
            resid = y_data - y_pred
            ssr = np.sum(resid**2)
            k = len(popt) # 参数数量
            n_samples = len(y_data)
            
            # 防止 log(0)
            if ssr <= 0: ssr = 1e-10
            
            aic = 2 * k + n_samples * np.log(ssr / n_samples)
            bic = n_samples * np.log(ssr / n_samples) + k * np.log(n_samples)
            
            fit_report[name] = {
                "r2": r2,
                "aic": aic,
                "bic": bic,
                "params": popt.tolist(),
                "y_pred": y_pred # 用于画图，暂存
            }
            
            # 使用 R2 作为主要评判标准 (也可以改成 if bic < best_bic)
            if r2 > best_score:
                best_score = r2
                best_model_name = name
                
        except Exception as e:
            print(f"模型 {name} 拟合失败: {e}")
            fit_report[name] = {"r2": -np.inf, "success": False}

    print(f"分析完成。最佳拟合模型: {best_model_name} (R2={best_score:.4f})")
    
    # --- 绘图与报告保存 ---
    
    # 1. 绘制最佳拟合图
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, color='black', alpha=0.5, label='Actual Data')
    
    if best_model_name in fit_report:
        best_info = fit_report[best_model_name]
        # 重新计算平滑曲线用于绘图
        x_smooth = np.linspace(min(x_data), max(x_data), 500)
        y_smooth = MODELS[best_model_name](x_smooth, *best_info['params'])
        
        plt.plot(x_smooth, y_smooth, 'r-', linewidth=2, 
                 label=f'{best_model_name} ($R^2={best_info["r2"]:.3f}$)')
        
    plt.title(f"Time Complexity Analysis: {file_name}")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(result_dir, "best_fit.png"))
    plt.close()
    
    # 2. 保存详细 JSON 报告
    # 移除 y_pred 以便序列化
    json_report = {}
    for k, v in fit_report.items():
        if "y_pred" in v:
            del v["y_pred"]
        json_report[k] = v
        
    with open(os.path.join(result_dir, "analysis_report.json"), 'w') as f:
        json.dump(json_report, f, indent=2)

    # 3. 验证是否符合预期
    # 将模型名称归一化比较 (忽略大小写等差异)
    is_success = False
    if best_model_name != "None":
        # 简单检查：如果最佳模型名称包含在预期列表中（模糊匹配）
        # 例如：expected=['linear'], best='Linear' -> Pass
        # 或者 expected=['logn'], best='Logarithmic' -> 需要映射
        
        # 建立简单的别名映射
        aliases = {
            'Logarithmic': ['logn', 'logarithmic', 'log'],
            'Linear': ['linear', 'o(n)'],
            'Quadratic': ['quadratic', 'o(n^2)'],
            'Cubic': ['cubic', 'o(n^3)'],
            'N Log N': ['nlogn', 'n_log_n']
        }
        
        # 检查
        cleaned_best = best_model_name
        
        for expected in expected_models:
            expected_lower = expected.lower()
            # 直接匹配
            if expected_lower == cleaned_best.lower():
                is_success = True
                break
            # 别名匹配
            if cleaned_best in aliases:
                if expected_lower in aliases[cleaned_best]:
                    is_success = True
                    break
                    
    return is_success

# ==========================================
# 3. 主程序入口
# ==========================================

def main():
    # 全局统计
    global_stats = {
        'total': 0, 'success': 0, 'failed': 0, 
        'failed_files': []
    }
    
    # 配置要运行的文件夹类型
    # folder_type = 'linear'  
    # 可以在这里修改，或者通过命令行参数传入
    folder_type = 'linear' 

    # 使用字典映射减少重复的if-elif结构
    folder_config = {
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

    # 获取文件列表
    if not os.path.exists(folder_path):
        print(f"文件夹不存在: {folder_path}")
        return
        
    python_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.py')])
    total_files = len(python_files)
    global_stats['total'] = total_files
    
    print(f"找到 {total_files} 个文件，开始处理...")
    
    # 根据folder_type确定基础目录
    base_dir_map = {
        'logn': config.logn_results_base_dir,
        'linear': config.linear_results_base_dir,
        'quadratic': config.quadratic_results_base_dir,
        'cubic': config.cubic_results_base_dir,
        'nlogn': config.nlogn_results_base_dir
    }
    base_dir = base_dir_map.get(folder_type, config.linear_results_base_dir)
                     
    for i, file_name in enumerate(python_files, 1):
        if(i>=0):
            full_path = os.path.join(folder_path, file_name)
            print(f"\n[{i}/{total_files}] 处理文件: {file_name}")
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

    # 最终统计
    print("\n" + "="*50)
    print("最终统计报告")
    print("="*50)
    print(f"总文件数: {global_stats['total']}")
    print(f"成功匹配: {global_stats['success']}")
    print(f"失败/不匹配: {global_stats['failed']}")
    if global_stats['failed_files']:
        print("\n失败文件列表:")
        for f in global_stats['failed_files'][:10]: # 只显示前10个
            print(f" - {f}")
        if len(global_stats['failed_files']) > 10:
            print(f" ... 等共 {len(global_stats['failed_files'])} 个")
            
    # 保存统计结果
    # 使用字典映射减少重复的if-elif结构
    # base_dir_map = {
    #     'logn': config.logn_results_base_dir,
    #     'linear': config.linear_results_base_dir,
    #     'quadratic': config.quadratic_results_base_dir,
    #     'cubic': config.cubic_results_base_dir,
    #     'nlogn': config.nlogn_results_base_dir
    # }
    # base_dir = base_dir_map.get(folder_type, config.logn_results_base_dir)  # 默认路径
    
    stats_path = os.path.join(base_dir, f"stats_{folder_type}.json")
    with open(stats_path, 'w') as f:
        json.dump(global_stats, f, indent=2)
    print(f"\n统计已保存至: {stats_path}")

if __name__ == "__main__":
    main()