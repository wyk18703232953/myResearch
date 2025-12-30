from collections import defaultdict as dd, deque as dq
import math
import random

MOD = 10**9 + 7

"""
原始题意（从注释中推导）：
x*(x+1)//2 个糖果被放入盒子
N - x 个糖果被吃掉
盒中剩下 K 个糖果

由题注中的推导公式：
x*(x+1)//2 + x - N - K = 0
=> x**2 + 3*x - 2*(N + K) = 0
=> x = (-3 + sqrt(9 + 8*(N+K))) // 2

原程序：给定 N, K，计算并输出  x*(x+1)//2 - K
"""

def solve(N, K):
    x = int((-3 + math.isqrt(9 + 8 * (N + K))) // 2)
    return x * (x + 1) // 2 - K

def main(n):
    """
    n 为规模参数，用来控制生成的 N、K 的大小。
    这里简单生成：
        1 <= N <= n
        0 <= K <= N
    然后调用 solve(N, K) 并打印结果。
    """
    if n < 1:
        n = 1

    # 生成测试数据
    N = random.randint(1, n)
    K = random.randint(0, N)

    # 调用原逻辑
    ans = solve(N, K)

    # 输出结果（模拟原程序仅输出答案）
    print(ans)

if __name__ == "__main__":
    # 示例：可根据需要修改 n 的默认值
    main(10)