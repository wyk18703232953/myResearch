import random

def main(n: int):
    # 生成测试数据：m 为 1..n 之间的随机值，arr 为 0..10^9 之间的随机整数
    if n <= 0:
        return
    m = random.randint(1, n)
    arr = [random.randint(0, 10**9) for _ in range(n)]

    dp = [[] for _ in range(m)]
    for i in range(n):
        dp[arr[i] % m].append(i)

    res = 0
    k = n // m
    ans = arr.copy()
    s = []
    for _ in range(2):
        for i in range(m):
            if len(dp[i]) < k:
                while s and len(dp[i]) < k:
                    x = s.pop()
                    y = arr[x] % m
                    if i > y:
                        ans[x] = ans[x] + (i - y)
                        res = res + (i - y)
                    else:
                        ans[x] = ans[x] + (m - 1 - y) + (i + 1)
                        res = res + (m - 1 - y) + (i + 1)
                    dp[i].append("xxx")
            if len(dp[i]) > k:
                while len(dp[i]) > k:
                    s.append(dp[i].pop())

    print(res)
    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)