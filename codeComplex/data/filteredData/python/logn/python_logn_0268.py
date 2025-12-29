import random

base = 10**9 + 7

def get2k(k):
    f = 2
    b = 1
    r = 1
    while k >= b:
        if k & b > 0:
            r = r * f % base
        b *= 2
        f = f * f % base
    return r

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单选择 x, k 都在 [0, n] 范围内随机生成
    # 你可以根据需要调整生成策略
    x = random.randint(0, n)
    k = random.randint(0, n)

    if x == 0:
        print(0)
        return

    t2k = get2k(k)
    r = x * t2k * 2 - t2k + 1
    r %= base
    print(r)

if __name__ == "__main__":
    # 示例：使用规模 n=10 运行一次
    main(10)