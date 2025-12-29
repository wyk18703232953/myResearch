def main(n: int):
    # 根据 n 生成测试数据 (n, a, b)
    # 这里给出一个简单的可调策略：
    # - 若 n < 3: 用 a=1,b=1（总是可行）
    # - 若 n 为奇数且 >= 3: a=1,b=2
    # - 若 n 为偶数且 >= 4: a=2,b=1
    if n < 3:
        a, b = 1, 1
    elif n % 2 == 1:
        a, b = 1, 2
    else:
        a, b = 2, 1

    if min(a, b) > 1 or (1 < n < 4 and max(a, b) == 1):
        print('NO')
        return

    print('YES')
    f = int(a == 1)
    g = [a, b][f]
    r = [[f] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 0
    for i in range(n - g):
        r[i][i + 1] ^= 1
        r[i + 1][i] ^= 1
    for x in r:
        print(*x, sep='')


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(5)