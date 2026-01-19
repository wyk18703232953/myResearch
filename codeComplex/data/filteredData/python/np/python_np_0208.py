def main(n):
    # 映射规模 n 到原题参数：
    # 使用 n 作为题目中的 n（任务数量）
    # l, r, x 为确定性构造
    if n <= 0:
        print(0)
        return

    # 任务难度列表：tasks[i] = i + 1，长度为 n
    tasks = [i + 1 for i in range(n)]

    # 设定约束区间和难度差
    # l: 至少要两任务之和的大小级别
    # r: 上界是前 n 个正整数和
    total_sum = n * (n + 1) // 2
    l = max(3, n)                   # 至少要有一定和
    r = total_sum                   # 最大可能和
    x = max(1, n // 4)              # 最小难度差

    mask = 3  # 最小的包含至少两个最低位的子集掩码
    ans = 0

    while mask < (1 << n):
        sum_dif = 0
        min_diff = float("inf")
        max_diff = -float("inf")

        # 至少包含两个任务时才考虑
        if mask & (mask - 1):
            for i in range(n):
                if mask & (1 << i):
                    sum_dif += tasks[i]
                    if tasks[i] < min_diff:
                        min_diff = tasks[i]
                    if tasks[i] > max_diff:
                        max_diff = tasks[i]
            if (x <= (max_diff - min_diff)) and (l <= sum_dif <= r):
                ans += 1

        mask += 1

    print(ans)


if __name__ == "__main__":
    main(10)