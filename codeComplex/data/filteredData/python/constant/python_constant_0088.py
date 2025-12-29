import sys
from math import gcd

mod = 10**9 + 7
mod2 = 998244353

def l1d(n, val=0): 
    return [val for _ in range(n)]

def l2d(n, m, val=0): 
    return [l1d(n, val) for _ in range(m)]

def pmat(A):
    for ele in A:
        print(*ele, end="\n")

def main(n):
    """
    n 作为规模参数：
    本题原程序逻辑：给定一个整数 x，输出不超过 x 的三个正整数的最大 lcm。
    这里直接用 n 作为原程序中的 x。
    """
    x = n

    if x <= 2:
        print(x)
        return

    if x % 2 == 1:
        # 原代码：x 为奇数时直接用 x, x-1, x-2 的 lcm
        a = x
        lcm_val = a * (a - 1) // gcd(a, a - 1)
        lcm_val = lcm_val * (a - 2) // gcd(lcm_val, a - 2)
        print(lcm_val)
    else:
        # 原代码：x 为偶数时在 [max(1,x-50), x] 上三重循环暴力求最大 lcm
        ans = 1
        low = max(1, x - 50)
        high = x
        for n1 in range(low, high + 1):
            for n2 in range(low, high + 1):
                for n3 in range(low, high + 1):
                    lcm12 = (n1 * n2) // gcd(n1, n2)
                    lcm123 = (lcm12 * n3) // gcd(lcm12, n3)
                    if lcm123 > ans:
                        ans = lcm123
        print(ans)

if __name__ == "__main__":
    # 示例：自动生成一个规模为 100 的测试
    # 可根据需要修改 n 的默认测试值
    test_n = 100
    main(test_n)