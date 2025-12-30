from collections import defaultdict
import random

def main(n: int):
    # 生成测试数据：两行长度为 n 的由 '0' 和 'X' 组成的字符串
    # 可根据需要调整生成规则
    S = []
    for _ in range(2):
        s = ''.join(random.choice(['0', 'X']) for _ in range(n))
        S.append(s)

    # 原逻辑开始
    S[0] = S[0].replace('X', '1')
    S[1] = S[1].replace('X', '1')

    n = len(S[0])
    if n == 1:
        print(0)
        return

    INF = 10 ** 18
    dp = defaultdict(lambda: -INF)
    for i in range(0, 2):
        for j in range(0, 2):
            dp[(i, j)] = -INF
    dp[(int(S[0][0]), int(S[1][0]))] = 0

    for i in range(1, n):
        nx = defaultdict(lambda: -INF)
        # 转移1：直接继承
        for j in range(0, 2):
            for k in range(0, 2):
                nx[(int(S[0][i]), int(S[1][i]))] = max(
                    nx[(int(S[0][i]), int(S[1][i]))],
                    dp[(j, k)]
                )
        # 转移2：根据规则增加
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
    for _, v in dp.items():
        ans = max(ans, v)
    print(ans)


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)