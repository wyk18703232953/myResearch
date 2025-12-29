import random

mod = 10**9 + 7

def main(n):
    # 1. 生成测试数据
    # 生成 n 首歌，每首歌有 (time, genre)
    # time: 1 到 n 之间的随机整数
    # genre: 3 种类型中的一种（0,1,2）
    a = []
    total_time = 0
    for _ in range(n):
        time = random.randint(1, n)
        genre = random.randint(0, 2)
        a.append((time, genre))
        total_time += time

    # 为了让目标总时间 t 有一定概率可行，
    # 我们从 [0, total_time] 中随机选择 t
    t = random.randint(0, total_time)

    # 2. 原逻辑：按总时长为 t 的合法排列计数
    dp = [[0 for _ in range(3)] for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][a[i][1]] = 1

    for i in range(1 << n):
        for j in range(3):
            if dp[i][j] == 0:
                continue
            mask = 1
            for k in range(n):
                if (i & mask) or (a[k][1] == j):
                    mask <<= 1
                    continue
                dp[i | mask][a[k][1]] = (dp[i | mask][a[k][1]] + dp[i][j]) % mod
                mask <<= 1

    ans = 0
    for i in range(1 << n):
        mask = 1
        duration = 0
        for j in range(n):
            if i & mask:
                duration += a[j][0]
            mask <<= 1
        if duration == t:
            ans = (ans + sum(dp[i])) % mod

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(n) 运行
    main(5)