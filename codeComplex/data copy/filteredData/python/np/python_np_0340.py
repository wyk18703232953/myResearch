def main(n):
    MOD = 10**9 + 7
    # 定义时间上限规模，保证随 n 增大而增大
    tnow = max(1, n * 2)

    # 构造 n 个任务 (duration, genre)，完全确定性
    # 持续时间为 i+1，类型为 i % 4
    arr = [[i + 1, i % 4] for i in range(n)]

    left = int("".join(["1" for _ in range(n)]), 2)
    dp = {}

    def recur(tnow_local, prevgenre, left_local):
        key = (left_local, prevgenre, tnow_local)
        if tnow_local == 0:
            return 1
        if key in dp:
            return dp[key]
        ans = 0
        for i in range(n):
            if (left_local & (1 << i)) != 0:
                duration, genre = arr[i]
                if duration <= tnow_local and genre != prevgenre:
                    new_left = left_local & (~(1 << i))
                    ans += recur(tnow_local - duration, genre, new_left)
        dp[key] = ans % MOD
        return dp[key]

    result = recur(tnow, 4, left) % MOD
    print(result)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 规模
    main(5)