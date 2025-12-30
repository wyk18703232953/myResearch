import random

MOD = 1000000007

def pow2(k):
    if k == 0:
        return 1
    z = pow2(k // 2)
    if k % 2 == 1:
        return (2 * z * z) % MOD
    else:
        return (z * z) % MOD

def main(n):
    """
    n: 控制测试数据规模，这里用于控制生成的 k 的大小范围。
       示例策略：
       - x 在 [0, 10^9] 随机生成
       - k 在 [0, n] 随机生成
    """
    # 生成测试数据
    x = random.randint(0, 10**9)
    k = random.randint(0, max(0, n))

    if x == 0:
        print(0)
        return

    t = pow2(k)
    a = x * t
    b = a - t + 1
    print((a + b) % MOD)

if __name__ == "__main__":
    # 可以在此处指定一个规模，例如 n = 10^6
    main(10**6)