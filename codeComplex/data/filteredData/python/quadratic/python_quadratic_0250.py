def main(n):
    # 根据 n 生成确定性的 a, b
    # 保证 a, b >= 1
    a = n % 5 + 1
    b = (n // 3) % 5 + 1

    if min(a, b) > 1 or (1 < n < 4 and max(a, b) == 1):
        # print('NO')
        pass
        return
    # print('YES')
    pass
    f = int(a == 1)
    g = [a, b][f]
    r = [[f] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 0
    for i in range(n - g):
        r[i][i + 1] ^= 1
        r[i + 1][i] ^= 1
    # print('\n'.join(''.join(map(str, row)) for row in r))
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 以进行规模实验
    main(5)