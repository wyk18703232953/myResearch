def main(n):
    # 映射：输入的 n -> 原程序中的 (n, a, b)
    # 为了可扩展和可重复，这里定义确定性生成规则：
    # - n >= 3
    # - a 固定为 1
    # - b 随 n 变化，但保持合法避免直接输出 NO 的情况
    #   使用一个简单的周期构造：b = 1 if n % 4 in (0, 3) else 2
    if n < 3:
        n = 3

    a = 1
    if n % 4 in (0, 3):
        b = 1
    else:
        b = 2

    if min(a, b) > 1 or 1 < n < 4 and max(a, b) == 1:
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
    # 示例调用，可根据需要调整规模
    main(5)