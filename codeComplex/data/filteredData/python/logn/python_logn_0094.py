import random

SIZE = 105


def main(n: int):
    """
    n: 控制测试数据规模（这里作为生成 l, r 的最大值的指数）
       例如 n=10，则生成的 l, r 在 [0, 2^10) 内
    """
    a = [0] * SIZE
    b = [0] * SIZE

    # 根据 n 生成测试数据
    # 保证 l <= r，且范围在 [0, 2^n)
    upper = 1 << max(1, n)  # 至少 2^1，避免全为 0 过于无意义
    l = random.randrange(0, upper)
    r = random.randrange(l, upper)

    if l == r:
        print(0)
        return

    len1 = 0
    len2 = 0

    tmp_l = l
    tmp_r = r

    while tmp_l != 0:
        a[len1] = tmp_l % 2
        tmp_l //= 2
        len1 += 1

    while tmp_r != 0:
        b[len2] = tmp_r % 2
        tmp_r //= 2
        len2 += 1

    tag = 0
    for i in range(max(len1, len2) - 1, 0, -1):
        if b[i] == 1 and a[i] == 0:
            tag = i
            break

    print(pow(2, tag + 1) - 1)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)