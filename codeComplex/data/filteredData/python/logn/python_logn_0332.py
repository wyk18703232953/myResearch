# -*- coding: utf-8 -*-
"""
将原始含 input() 的程序改为无 input()、可参数化规模 n 的版本。
根据 n 生成测试数据：
  假定 n 为测试数据组数，第 i 组为：
    x = i
    k = i
"""

MOD = 1000000007

def solve_one(x, k):
    if x == 0:
        return 0
    y = pow(2, k, MOD) * (2 * x - 1) + 1
    return y % MOD

def main(n):
    """
    n: 规模参数，这里表示要生成的测试数据组数。
    对于 i in [1..n]，生成 (x=i, k=i)，并计算并打印结果。
    """
    for i in range(1, n + 1):
        x = i
        k = i
        ans = solve_one(x, k)
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例：当 n = 5 时，生成 5 组测试数据并输出结果
    main(5)