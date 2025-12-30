import random

def main(n):
    # 生成测试数据
    # tnow 为总时间规模；这里简单生成为任务时间总和的一半左右
    arr = []
    total_time = 0
    for _ in range(n):
        a = random.randint(1, 10)     # 任务所需时间
        b = random.randint(0, 3)      # 任务类型(genre)
        arr.append([a, b])
        total_time += a
    tnow = max(1, total_time // 2)

    left = int("".join(["1" for _ in range(n)]), 2)
    dp = {}

    def recur(tnow, prevgenre, left_mask):
        key = str(left_mask) + "_" + str(prevgenre) + "_" + str(tnow)
        if tnow == 0:
            return 1
        if key in dp:
            return dp[key]

        ans = 0
        for i in range(n):
            if (left_mask & (1 << i)) != 0:
                if arr[i][0] <= tnow and arr[i][1] != prevgenre:
                    new_left = left_mask & (~(1 << i))
                    ans += recur(tnow - arr[i][0], arr[i][1], new_left)
        dp[key] = ans
        return ans

    MOD = 10**9 + 7
    result = recur(tnow, 4, left) % MOD
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模为 5
    main(5)