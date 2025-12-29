import random

def main(n: int):
    # 生成规模为 n 的测试数据 A
    # 这里生成 1 到 3 之间的随机整数，可按需要修改
    A = [random.randint(1, 3) for _ in range(n)]

    DP = [[-1] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        DP[i][i] = A[i]

    for mid in range(1, n):
        for i in range(n):
            j = i + mid
            if j == n:
                break
            for k in range(i, j + 1):
                if DP[i][k] == DP[k + 1][j] and DP[i][k] != -1:
                    DP[i][j] = DP[i][k] + 1

    ANS = [2000] * (n + 1)
    ANS.append(0)
    for i in range(0, n):
        ANS[i] = min(ANS[i], ANS[i - 1] + 1)
        for j in range(i, n):
            if DP[i][j] != -1:
                ANS[j] = min(ANS[j], ANS[i - 1] + 1)

    print(ANS[n - 1])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)