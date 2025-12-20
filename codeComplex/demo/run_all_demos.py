import subprocess
import os
import sys
import concurrent.futures

# 定义要运行的脚本列表
scripts = [
    r"d:\MyResearch\codeComplex\demo\onlyCode\scripts\consatnt_demo.py",
    r"d:\MyResearch\codeComplex\demo\onlyCode\scripts\cubic_demo.py",
    r"d:\MyResearch\codeComplex\demo\onlyCode\scripts\linear_demo.py",
    r"d:\MyResearch\codeComplex\demo\onlyCode\scripts\log_demo.py",
    r"d:\MyResearch\codeComplex\demo\onlyCode\scripts\nlong_demo.py",
    r"d:\MyResearch\codeComplex\demo\onlyCode\scripts\np_demo.py",
    r"d:\MyResearch\codeComplex\demo\onlyCode\scripts\quadratic_demo.py"
]

def run_script(script_path):
    """运行单个脚本并返回结果"""
    script_name = os.path.basename(script_path)
    try:
        # 注意：这里的print不会立即显示，因为子线程输出会混在一起
        result = subprocess.run(
            [sys.executable, script_path],
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=None
        )
        return {
            'script_name': script_name,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        }
    except Exception as e:
        return {
            'script_name': script_name,
            'stdout': '',
            'stderr': str(e),
            'returncode': -1
        }

def main():
    """主函数，使用ThreadPoolExecutor并行运行所有脚本"""
    print("开始并行运行所有演示脚本...")
    print("=" * 60)
    
    # 使用ThreadPoolExecutor而不是ProcessPoolExecutor
    # 限制最大并发数，通常为CPU核心数
    max_workers = min(len(scripts), os.cpu_count() or 4)
    print(f"使用线程池，最大并发数: {max_workers}")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有脚本任务
        future_to_script = {
            executor.submit(run_script, script): script 
            for script in scripts
        }
        
        print("所有脚本已提交，正在并行运行...")
        print("=" * 60)
        
        # 收集所有任务结果
        results = []
        completed = 0
        for future in concurrent.futures.as_completed(future_to_script):
            script = future_to_script[future]
            script_name = os.path.basename(script)
            
            try:
                result = future.result(timeout=None)
                results.append(result)
                completed += 1
                print(f"[{completed}/{len(scripts)}] {script_name} 完成")
            except Exception as e:
                print(f"{script_name} 执行出错: {e}")
    
    # 输出所有结果
    print("\n" + "="*60)
    print("执行结果汇总:")
    print("="*60)
    
    for result in results:
        script_name = result['script_name']
        
        print(f"\n{script_name}:")
        print(f"  返回码: {result['returncode']}")
        
        if result['stdout'] and result['stdout'].strip():
            output = result['stdout'].strip()
            if len(output) > 200:
                output = output[:200] + "..."
            print(f"  输出: {output}")
        
        if result['stderr'] and result['stderr'].strip():
            error = result['stderr'].strip()
            if len(error) > 200:
                error = error[:200] + "..."
            print(f"  错误: {error}")
        
        print("-" * 40)
    
    print(f"\n总共完成: {len(results)}/{len(scripts)} 个脚本")

if __name__ == "__main__":
    main()