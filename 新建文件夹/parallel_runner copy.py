import subprocess
import sys

python_exe = sys.executable  # 自动使用当前 Python 解释器
scripts = [f"script{i}.py" for i in range(1, 3)]

print("开始并行执行8个Python脚本...")

# 启动所有进程（非阻塞）
processes = []
for script in scripts:
    print(f"开始执行: {script}")
    p = subprocess.Popen(
        [python_exe, script],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    processes.append((script, p))

# 等待所有进程完成，并收集输出
for script, p in processes:
    stdout, stderr = p.communicate()  # 阻塞直到该进程结束
    print(f"\n{script} 执行完成")
    print(f"{script} 标准输出:")
    print(stdout)
    if stderr:
        print(f"{script} 错误输出:")
        print(stderr)

print("\n所有脚本执行完成！")