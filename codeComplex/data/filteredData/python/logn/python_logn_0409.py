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
    tests = []
    for _ in range(n):
        # 生成 n_i 和 k_i，可以根据需要调整范围
        ni = random.randint(1, 10**6)
        ki = random.randint(1, 10**6)
        tests.append((ni, ki))

    # 按原逻辑处理并输出
    for ni, ki in tests:
        a = solve(ni, ki)
        if a == -1:
            print('NO')
        else:
            print('YES', a)


if __name__ == "__main__":
    # 示例：运行 5 组测试
    main(5)