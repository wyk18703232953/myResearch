import random

def main(n):
    # 生成测试数据：随机选择 m，范围为 1..n（也可以按需修改）
    m = random.randint(1, n)

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
    # 示例：调用 main(5) 进行测试
    main(5)