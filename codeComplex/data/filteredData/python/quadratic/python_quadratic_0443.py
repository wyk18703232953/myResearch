import random

def main(n: int):
    # 生成长度为 n 的测试数据 A，可按需修改生成规则
    A = [random.randint(1, 100) for _ in range(n)]

    dp = [[1 for _ in range(5)] for _ in range(n)]
    Prev = [[-1 for _ in range(5)] for _ in range(n)]

    for i in range(1, n):
        for j in range(5):
            for finger in range(5):
                if dp[i - 1][finger] == 1:
                    if ((A[i - 1] < A[i] and finger < j) or
                        (A[i - 1] > A[i] and finger > j) or
                        (A[i - 1] == A[i] and finger != j)):
                        dp[i][j] = 1
                        Prev[i][j] = finger
                        break
            else:
                dp[i][j] = 0

    finger = 0
    for j in range(5):
        if dp[-1][j] == 1:
            finger = j
            path = [finger]
            for i in range(n - 1, 0, -1):
                finger = Prev[i][finger]
                path.append(finger)
            path = path[::-1]
            for i in range(n):
                print(path[i] + 1, end=' ')
            print()
            break
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：n = 10，可按需修改或在外部调用 main(n)
    main(10)