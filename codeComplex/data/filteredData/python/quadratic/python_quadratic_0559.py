import random

def main(n):
    # 根据 n 生成测试数据，这里设置 m 与 n 同规模
    m = n

    r = []
    rappend = r.append
    for i in range(1, (n >> 1) + 1):
        for j in range(1, m + 1):
            rappend(str(i) + ' ' + str(j))
            rappend(str(n + 1 - i) + ' ' + str(m + 1 - j))

    if n & 1:
        for i in range(1, (m >> 1) + 1):
            rappend(str((n + 1) >> 1) + ' ' + str(i))
            rappend(str((n + 1) >> 1) + ' ' + str(m + 1 - i))
        if m & 1:
            rappend(str((n + 1) >> 1) + ' ' + str((m + 1) >> 1))

    print('\n'.join(r))


if __name__ == "__main__":
    # 示例：自动生成一个规模 n（例如 1 到 10 之间的随机数）
    n = random.randint(1, 10)
    main(n)