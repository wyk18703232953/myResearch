import math as mt
import random

# 常量 p 在原代码中使用到，用作 nCr 预处理的模数，这里保留
p = 10**9 + 7

# 预处理数组，保持与原代码一致的上限
MAXN = 300001
inv = [0] * MAXN
fact = [0] * MAXN

def ncr_util():
    inv[0] = inv[1] = 1
    fact[0] = fact[1] = 1
    for i in range(2, MAXN):
        inv[i] = (inv[i % p] * (p - p // i)) % p
    for i in range(1, MAXN):
        inv[i] = (inv[i - 1] * inv[i]) % p
        fact[i] = (fact[i - 1] * i) % p

def solve(n, k):
    a = 1
    b = 2 * n + 3
    c = n + n * n - 2 * k
    disc = b * b - 4 * a * c
    root = int(mt.isqrt(disc))  # 更安全的整数平方根
    x1 = b + root
    x2 = b - root
    if x1 % 2 == 0 and x1 // 2 <= n:
        return x1 // 2
    return x2 // 2

def main(n):
    # 可根据需要初始化组合数相关预处理
    # ncr_util()  # 若后续需要使用 fact 与 inv，可取消注释

    # 根据规模 n 生成测试数据 (n, k)
    # 这里设定 k 的合理范围为 [0, n^2]，以避免判别式为负
    if n <= 0:
        n = 1
    max_k = n * n
    k = random.randint(0, max_k)

    ans = solve(n, k)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)