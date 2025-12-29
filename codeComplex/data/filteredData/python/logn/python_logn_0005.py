import random

def main(n: int):
    # 生成规模为 n 的测试数据：随机生成两个位数不超过 n 的非负整数
    # 为了可控，这里让 a, b < 2^n
    if n <= 0:
        a, b = 0, 0
    else:
        limit = 1 << n
        a = random.randrange(limit)
        b = random.randrange(limit)

    # 原逻辑开始
    if a == b:
        print(0)
    else:
        x = a ^ b
        c = 1
        while x:
            x >>= 1
            c <<= 1
        print(c - 1)

if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)