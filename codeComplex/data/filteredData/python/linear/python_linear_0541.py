def main(n):
    # 生成确定性的数组 A，长度为 n
    # 示例：A[i] = (-1)^i * (i + 1)
    A = [(-(i + 1) if i % 2 else (i + 1)) for i in range(n)]

    if n == 0:
        # print(0)
        pass
    elif n == 1:
        # print(A[0])
        pass
    elif n == 2:
        # print(abs(A[0] - A[1]))
        pass

    else:
        SUM = 0
        for i in range(n):
            SUM += abs(A[i])
        ANS = 0

        for i in range(n - 1):
            candidate = SUM - abs(A[i]) - abs(A[i + 1]) + abs(A[i] - A[i + 1])
            if ANS < candidate:
                ANS = candidate

        # print(ANS)
        pass
if __name__ == "__main__":
    # 示例：使用 n = 10 进行运行
    main(10)