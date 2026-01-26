def main(n):
    if n <= 0:
        return
    # 构造确定性的输入数组 arr，长度为 n
    # 为了覆盖各种关系情况，这里定义一个简单的循环模式：
    # 3, 1, 2, 2, 5, 4, 4, 6, ...
    base = [3, 1, 2, 2, 5, 4]
    arr = [base[i % len(base)] + (i // len(base)) for i in range(n)]

    dp = [[-1 for _ in range(5 + 1)] for _ in range(n)]
    for i in range(1, 6):
        dp[0][i] = 1

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            for j in range(1, 6):
                for k in range(1, j):
                    if dp[i - 1][k] == 1:
                        dp[i][j] = 1
                        break
        elif arr[i] < arr[i - 1]:
            for j in range(1, 6):
                for k in range(j + 1, 6):
                    if dp[i - 1][k] == 1:
                        dp[i][j] = 1
                        break

        else:
            for j in range(1, 6):
                for k in range(1, 6):
                    if j == k:
                        continue
                    if dp[i - 1][k] == 1:
                        dp[i][j] = 1
                        break

    ans = []
    for i in range(1, 6):
        if dp[n - 1][i] == 1:
            ans.append(i)
            break

    if len(ans) == 0:
        # print(-1)
        pass
        return

    for i in range(n - 2, -1, -1):
        curr = ans[-1]
        if arr[i] > arr[i + 1]:
            for j in range(curr + 1, 6):
                if dp[i][j] == 1:
                    ans.append(j)
                    break
        elif arr[i] < arr[i + 1]:
            for j in range(1, curr):
                if dp[i][j] == 1:
                    ans.append(j)
                    break

        else:
            for j in range(1, 6):
                if j == curr:
                    continue
                if dp[i][j] == 1:
                    ans.append(j)
                    break

    ans = ans[::-1]
    # print(*ans)
    pass
if __name__ == "__main__":
    main(10)