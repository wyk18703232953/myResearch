import random


def sol(n, m):
    v = [0 for _ in range(n + 1)]
    left, right = 1, n
    for i in range(1, n + 1):
        if n - i - 1 <= 0:
            pw = 1
        else:
            pw = 1 << (n - i - 1)

        if m <= pw:
            v[left] = i
            left += 1
        else:
            v[right] = i
            right -= 1
            m -= pw
    return [' '.join(map(str, v[1:]))]


def main(n):
    # 根据 n 生成测试数据：
    # m 的范围推导自原逻辑：最大需要的 m 不超过 2^(n-1)
    if n <= 0:
        return

    max_m = 1 << (n - 1)
    m = random.randint(1, max_m)

    for line in sol(n, m):
        print(line)


if __name__ == '__main__':
    # 示例：调用 main，规模可自行调整
    main(5)