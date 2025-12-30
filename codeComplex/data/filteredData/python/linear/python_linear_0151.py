import random

def main(n, p=1000, seed=0):
    """
    n: 数据规模，即生成的数组长度
    p: 取模参数（需 > 0）
    seed: 随机种子，为了可复现
    """
    random.seed(seed)

    # 生成测试数据：a 中为非负整数，这里设置为 [0, 10^6)
    a = [random.randint(0, 10**6) for _ in range(n)]

    # 原始逻辑
    a_mod = [c % p for c in a]
    s = sum(a_mod)
    sp = s % p
    if sp == s or sp + 1 == p:
        print(sp)
    else:
        print(sp + p)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)