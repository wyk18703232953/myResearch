# parallel_runner.py - 多线程并行执行8个脚本
import multiprocessing
import subprocess
import os

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 要执行的脚本列表
scripts = [f"script{i}.py" for i in range(1, 3)]

def run_script(script_name):
    """执行单个Python脚本"""
    script_path = os.path.join(current_dir, script_name)
    print(f"开始执行: {script_name}")
    try:
        result = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            cwd=current_dir
        )
        print(f"{script_name} 执行完成")
        print(f"{script_name} 标准输出:")
        print(result.stdout)
        if result.stderr:
            print(f"{script_name} 错误输出:")
            print(result.stderr)
    except Exception as e:
        print(f"执行 {script_name} 时出错: {e}")

if __name__ == "__main__":
    print("开始并行执行8个Python脚本...")
    
    # 创建进程池，使用与CPU核心数相当的进程数
    pool = multiprocessing.Pool(processes=min(8, multiprocessing.cpu_count()))
    
    # 并行执行所有脚本
    pool.map(run_script, scripts)
    
    # 关闭进程池
    pool.close()
    pool.join()
    
    print("所有脚本执行完成！")