import time

# ================= 1. 定义 7 种复杂度的真实计算任务 =================

def task_O1(n):
    # O(1): 无论 n 多大，只做一次基础运算
    return n * 2 + 1

def task_O_log_n(n):
    # O(log n): 模拟二分查找或折半逻辑
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count

def task_O_n(n):
    # O(n): 单层循环
    count = 0
    for i in range(n):
        count += 1
    return count

def task_O_n_log_n(n):
    # O(n log n): 外层线性，内层折半
    count = 0
    for i in range(n):
        j = n
        while j > 1:
            j //= 2
            count += 1
    return count

def task_O_n2(n):
    # O(n^2): 双层嵌套循环
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

def task_O_n3(n):
    # O(n^3): 三层嵌套循环
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    return count

def task_O_2n(n):
    # O(2^n): 指数级循环。注意这里用 1 << n 快速计算 2^n
    count = 0
    for i in range(1 << n): 
        count += 1
    return count

# ================= 2. 核心测试逻辑 =================

def run_benchmark(task_func, task_name, n_val, runs=100):
    # 预热系统，防止初次运行的冷启动惩罚（如缓存未命中）
    for _ in range(5):
        task_func(n_val)
        
    execution_times = []
    
    # 正式跑 runs 次
    for _ in range(runs):
        start = time.perf_counter()
        task_func(n_val)
        end = time.perf_counter()
        execution_times.append(end - start)
    
    # 优化输出：显示统计信息而不是原始数据
    t_min = min(execution_times)
    t_max = max(execution_times)
    t_avg = sum(execution_times) / runs
    t_std = (sum((t - t_avg) ** 2 for t in execution_times) / runs) ** 0.5
    diff = t_max - t_min
    
    # 避免 O(1) 跑得太快导致分母为 0
    if t_min == 0: 
        t_min = 1e-9 
        
    disturbance_percent = (diff / t_min) * 100
    
    # 优化输出：显示详细的统计信息和每次耗时
    # print(f"\n{task_name} 测试结果 (n={n_val}, 运行{runs}次):")
    
    # 输出所有次耗时，用于分析离群值
    # print(f"  所有耗时 (共{runs}次):")
    # for i, t in enumerate(execution_times):
    #     if i % 10 == 0:
    #         print(f"\n    ", end="")
        
    #     # 标记最大耗时
    #     if t == t_max:
    #         print(f"[{t*1000000:6.1f}μs]", end="")  # 用方括号标记最大耗时
    #     else:
    #         print(f"{t*1000000:6.1f}μs", end="")
    # print()
    
    # print(f"  最小耗时: {t_min*1000000:8.2f} μs")
    # print(f"  最大耗时: {t_max*1000000:8.2f} μs") 
    # print(f"  平均耗时: {t_avg*1000000:8.2f} μs")
    # print(f"  标准差:   {t_std*1000000:8.2f} μs")
    # print(f"  波动范围: {diff*1000000:8.2f} μs ({disturbance_percent:6.2f}%)")
    # print(f"  数据分布: {t_min*1000000:.2f} - {t_max*1000000:.2f} μs")
    
    # 表格格式输出（保持原有格式）
    print(f"| {task_name:<10} | n={n_val:<10} | {t_min*1000000:>8.2f} μs | {t_max*1000000:>8.2f} μs | {disturbance_percent:>8.2f}% |")

# ================= 3. 执行全套测试 =================

if __name__ == "__main__":
    print("开始探测不同时间复杂度在物理环境中的真实扰动...")
    print("注意：绝对时间越短的任务，系统微小噪音引发的百分比扰动会越夸张！\n")
    
    print(f"| {'复杂度类别':<10} | {'测试规模 n':<10} | {'最小耗时(基准)':<10} | {'最大耗时(波动)':<10} | {'扰动比例':<9} |")
    print("-" * 65)
    
    # 分别设置不同的 n，使得每种任务大概运行几毫秒到几十毫秒
    run_benchmark(task_O1,       "O(1)",       10**5)          # n 再大也没用，只执行 1 次
    run_benchmark(task_O1,       "O(1)",       10**5)          # n 再大也没用，只执行 1 次
    run_benchmark(task_O1,       "O(1)",       10**5)          # n 再大也没用，只执行 1 次
    run_benchmark(task_O1,       "O(1)",       10**5)          # n 再大也没用，只执行 1 次
    run_benchmark(task_O1,       "O(1)",       10**5)          # n 再大也没用，只执行 1 次
    run_benchmark(task_O1,       "O(1)",       10**5)          # n 再大也没用，只执行 1 次
    run_benchmark(task_O1,       "O(1)",       10**5)          # n 再大也没用，只执行 1 次
    run_benchmark(task_O1,       "O(1)",       10**5)          # n 再大也没用，只执行 1 次
    run_benchmark(task_O_log_n,  "O(log n)",   10**18)         # 即使 n 是 100 亿亿，循环也只需 60 次
    run_benchmark(task_O_n,      "O(n)",       100000)         # 10 万次循环
    run_benchmark(task_O_n_log_n,"O(n log n)", 10000)          # 1 万 * log(1万) 次
    run_benchmark(task_O_n2,     "O(n^2)",     500)            # 500 * 500 = 25万次
    run_benchmark(task_O_n3,     "O(n^3)",     60)             # 60 * 60 * 60 = 21.6万次
    run_benchmark(task_O_2n,     "O(2^n)",     18)             # 2^18 = 26.2万次
    
    print("-" * 65)