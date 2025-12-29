from math import ceil
import random


def solve(n, k):
    if k == 1:
        return n - 1
    if k == 2:
        if n > 1:
            return n - 1
        else:
            return -1
    if k == 3:
        if n > 2:
            return n - 1
        else:
            return -1
    if k in {4, 5}:
        if n > 1:
            return n - 2
        else:
            return -1

    if 2 * n + 1 <= len(bin(3 * k)[2:]):
        return -1
    else:
        return n - ceil((len(bin(3 * k)[2:]) - 1) / 2)


def main(n):
    # 生成 n 组测试数据
    # n 作为组数，这里令每组的 n_i、k_i 也与 n 有关以便规模可控
    random.seed(0)
    for _ in range(n):
        # n_i 至少为 1，最大设为 2n
        ni = random.randint(1, 2 * n if 2 * n > 1 else 1)
        # k_i 至少为 1，最大设为 2n
        ki = random.randint(1, 2 * n if 2 * n > 1 else 1)
        a = solve(ni, ki)
        if a == -1:
            print('NO')
        else:
            print('YES', a)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)