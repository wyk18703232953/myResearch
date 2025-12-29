from math import sqrt
import random

def issq(p):
    x = int(sqrt(p))
    return x * x == p

def g(n):
    return (issq(n // 2) and n % 2 == 0) or (issq(n // 4) and n % 4 == 0)

def main(n):
    """
    n: 规模参数，用作测试样例数量 t
    根据 n 生成 n 个测试数据，并输出每个测试数据的结果。
    测试数据生成策略：在 1 到 10^9 之间随机生成整数。
    """
    random.seed(0)  # 固定种子，保证可复现
    t = n
    for _ in range(t):
        # 生成一个随机测试数据，范围可按需调整
        x = random.randint(1, 10**9)
        print("YES" if g(x) else "NO")


if __name__ == "__main__":
    # 可以在这里指定一个默认的 n 进行测试
    main(10)