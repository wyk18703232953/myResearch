import random

SIZE = 105


def main(n: int):
    """
    n 作为规模参数，用于生成测试数据。
    这里约定：生成的 l, r 为 0 <= l <= r < 2^n（且 n 不超过 60 之类的安全范围）。
    """

    # 生成测试数据：0 <= l <= r < 2^n
    upper = 1 << min(n, 60)  # 防止位运算溢出到非常大
    l = random.randrange(0, upper)
    r = random.randrange(l, upper)

    a = [0] * SIZE
    b = [0] * SIZE

    if l == r:
        print(0)
        return

    len1 = 0
    len2 = 0

    tmp = l
    while tmp != 0:
        a[len1] = tmp % 2
        tmp //= 2
        len1 += 1

    tmp = r
    while tmp != 0:
        b[len2] = tmp % 2
        tmp //= 2
        len2 += 1

    tag = 0
    for i in range(max(len1, len2) - 1, 0, -1):
        if b[i] == 1 and a[i] == 0:
            tag = i
            break

    print(pow(2, tag + 1) - 1)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)