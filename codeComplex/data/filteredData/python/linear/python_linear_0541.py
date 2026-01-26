def main(n):
    # 生成确定性输入：长度为 n 的整数数组 A
    # 这里选取简单的线性构造：A[i] = i - n//2
    if n <= 0:
        return
    A = [i - n // 2 for i in range(n)]

    if n == 1:
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
    # 示例调用：可以修改 n 来进行规模实验
    main(10)