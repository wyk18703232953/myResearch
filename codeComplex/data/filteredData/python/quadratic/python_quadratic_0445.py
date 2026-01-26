def main(n):
    if n <= 0:
        return
    # 确定性生成长度为 n 的数组 a
    # 模式：前半段非递减，后半段非增，掺杂相等元素
    a = []
    base = 1
    for i in range(n):
        if i < n // 3:
            val = base + (i % 3)
        elif i < 2 * n // 3:
            val = base + (n // 3) - (i - n // 3) // 2

        else:
            val = base + (n // 6) - (i - 2 * n // 3)
        a.append(val)

    dp = [[False, False, False, False, False] for _ in range(n)]
    dp[0] = [True, True, True, True, True]
    for i in range(1, n):
        for j in range(5):
            if a[i] == a[i - 1]:
                for k in range(5):
                    if k != j:
                        dp[i][j] = dp[i][j] or dp[i - 1][k]
            elif a[i] > a[i - 1]:
                for k in range(j):
                    dp[i][j] = dp[i][j] or dp[i - 1][k]

            else:
                for k in range(j + 1, 5):
                    dp[i][j] = dp[i][j] or dp[i - 1][k]
    if dp[-1].count(True) == 0:
        # print(-1)
        pass
        return
    j = 0
    for k in range(5):
        if dp[-1][k]:
            j = k
    ans = []
    for i in range(n - 1, -1, -1):
        ans.append(j + 1)
        if i == 0:
            break
        if a[i] == a[i - 1]:
            for k in range(5):
                if k != j and dp[i - 1][k]:
                    j = k
                    break
        elif a[i] > a[i - 1]:
            for k in range(j):
                if dp[i - 1][k]:
                    j = k
                    break

        else:
            for k in range(j + 1, 5):
                if dp[i - 1][k]:
                    j = k
                    break
    # print(*ans[::-1])
    pass
if __name__ == "__main__":
    main(10)