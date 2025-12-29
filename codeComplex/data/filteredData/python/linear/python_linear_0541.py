import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组 A
    # 这里示例为在 [-10^9, 10^9] 范围内随机生成
    A = [random.randint(-10**9, 10**9) for _ in range(n)]

    if n == 1:
        print(A[0])

    elif n == 2:
        print(abs(A[0] - A[1]))

    else:
        SUM = 0
        for i in range(n):
            SUM += abs(A[i])
        ANS = 0

        for i in range(n - 1):
            candidate = SUM - abs(A[i]) - abs(A[i + 1]) + abs(A[i] - A[i + 1])
            if ANS < candidate:
                ANS = candidate

        print(ANS)


# 示例调用
if __name__ == "__main__":
    main(5)