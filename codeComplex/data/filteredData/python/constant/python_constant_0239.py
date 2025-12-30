import random

def main(n: int):
    # 根据 n 生成测试数据，这里生成一个较大的随机整数 m
    # 例如：m 的比特长度设置为 n+5，保证对 2**n 取模有意义
    if n <= 0:
        n = 1
    bit_len = max(1, n + 5)
    m = random.getrandbits(bit_len)

    if n <= 26:
        print(m % (2 ** n))
    else:
        print(m)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时由外部传入 n
    main(10)