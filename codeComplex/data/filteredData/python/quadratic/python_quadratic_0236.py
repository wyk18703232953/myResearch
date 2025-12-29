import random

def main(n: int):
    # 生成测试数据：随机生成 s 和 c
    # s 为 1~1e9 的随机整数，c 为 1~1e3 的随机正整数
    s = [random.randint(1, 10**9) for _ in range(n)]
    c = [random.randint(1, 1000) for _ in range(n)]

    dp = [float('inf')] * n
    for i in range(1, n):
        mn = float('inf')
        for j in range(i):
            if s[i] > s[j]:
                mn = min(mn, c[i] + c[j])
        dp[i] = mn

    res = float('inf')
    for i in range(1, n):
        for j in range(i):
            if s[i] > s[j]:
                res = min(res, c[i] + dp[j])

    if res == float('inf'):
        res = -1

    print(res)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)