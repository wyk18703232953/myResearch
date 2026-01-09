import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def analyze_complexity(file_path):
    # 1. 读取数据
    try:
        data = np.load(file_path)
        # 获取数组（通常是第一个文件）
        arr = data[data.files[0]]
        x = arr[:, 0]  # 输入规模 n
        y = arr[:, 1]  # 时间/字节码
        
        # 排序以确保画图正确
        sorted_indices = np.argsort(x)
        x = x[sorted_indices]
        y = y[sorted_indices]
    except Exception as e:
        print(f"读取文件失败: {e}")
        return

    # 2. 定义候选函数模型
    def linear(n, a, b): return a * n + b
    def quadratic(n, a, b, c): return a * n**2 + c
    def cubic(n, a, b, c, d): return a * n**3 + d
    def n_log_n(n, a, b): return a * n * np.log(np.maximum(n, 1e-10)) + b
    def logarithmic(n, a, b): return a * np.log(np.maximum(n, 1e-10)) + b
    def exponential(n, a, b): return a * np.exp(b * n)

    models = {
        "线性 O(n)": linear,
        "二次方 O(n^2)": quadratic,
        "立方方 O(n^3)": cubic,
        "线性对数 O(n log n)": n_log_n,
        "对数 O(log n)": logarithmic
        # 指数模型通常用于极快增长，这里视情况可加入
    }

    print(f"{'模型名称':<15} | {'R² (拟合优度)':<15}")
    print("-" * 35)

    best_r2 = -np.inf
    best_name = ""
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='black', alpha=0.5, label='实际数据')

    # 3. 拟合与评估
    for name, func in models.items():
        try:
            # 尝试拟合
            popt, _ = curve_fit(func, x, y, maxfev=10000)
            y_pred = func(x, *popt)
            
            # 计算 R² (决定系数)
            ss_res = np.sum((y - y_pred) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            r2 = 1 - (ss_res / ss_tot)
            
            print(f"{name:<15} | {r2:.5f}")
            
            # 记录最佳模型
            if r2 > best_r2:
                best_r2 = r2
                best_name = name
                
            # 绘制曲线（仅绘制拟合较好的）
            if r2 > 0.8:
                plt.plot(x, y_pred, label=f"{name} (R²={r2:.3f})")
                
        except Exception:
            print(f"{name:<15} | 拟合失败")

    print("-" * 35)
    print(f"✅ 最符合的函数模型应该是: {best_name}")

    plt.title(f"时间复杂度拟合分析 (最佳: {best_name})")
    plt.xlabel("输入规模 (n)")
    plt.ylabel("时间 / 指令数")
    plt.legend()
    plt.grid(True)
    plt.show()

# 运行分析
analyze_complexity('time_results.npz')