def main(n):
    # n 表示两个字符串的长度
    if n <= 0:
        return

    S = []
    # 构造两个只包含 '0' 和 '1' 的确定性字符串，然后将 '0' 视作非 '1' 字符
    s0 = ''.join('1' if (i % 3 == 0) else '0' for i in range(n))
    s1 = ''.join('1' if (i % 2 == 0) else '0' for i in range(n))
    S.append(s0.replace('0', 'X').replace('X', '1'))  # 原代码会把 'X' 变成 '1'，这里保证字符集兼容
    S.append(s1.replace('0', 'X').replace('X', '1'))

    S[0] = S[0].replace('X', '1')
    S[1] = S[1].replace('X', '1')

    n_local = len(S[0])
    if n_local == 1:
        # print(0)
        pass
        return

    INF = 10 ** 18
    from collections import defaultdict
    dp = defaultdict(lambda: -INF)
    for i in range(0, 2):
        for j in range(0, 2):
            dp[(i, j)] = -INF
    dp[(int(S[0][0]), int(S[1][0]))] = 0

    for i in range(1, n_local):
        nx = defaultdict(lambda: -INF)
        for j in range(0, 2):
            for k in range(0, 2):
                nx[(int(S[0][i]), int(S[1][i]))] = max(nx[(int(S[0][i]), int(S[1][i]))], dp[(j, k)])
        for j in range(0, 2):
            for k in range(0, 2):
                if dp[(j, k)] == -INF:
                    continue
                if j == 0 and k == 0:
                    if S[0][i] == '1' and S[1][i] != '1':
                        nx[(1, 1)] = max(nx[(1, 1)], dp[(j, k)] + 1)
                    if S[0][i] != '1' and S[1][i] == '1':
                        nx[(1, 1)] = max(nx[(1, 1)], dp[(j, k)] + 1)
                    if S[0][i] != '1' and S[1][i] != '1':
                        nx[(1, 0)] = max(nx[(1, 0)], dp[(j, k)] + 1)
                        nx[(0, 1)] = max(nx[(0, 1)], dp[(j, k)] + 1)
                        nx[(1, 1)] = max(nx[(1, 1)], dp[(j, k)] + 1)
                if j == 0 and k == 1:
                    if S[0][i] != '1' and S[1][i] != '1':
                        nx[(1, 1)] = max(nx[(1, 1)], dp[(j, k)] + 1)
                if j == 1 and k == 0:
                    if S[0][i] != '1' and S[1][i] != '1':
                        nx[(1, 1)] = max(nx[(1, 1)], dp[(j, k)] + 1)
        dp = nx
    ans = -INF
    for k, v in dp.items():
        ans = max(ans, v)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：输入规模为 10
    main(10)