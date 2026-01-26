def main(n):
    # 映射：将 n 作为 N 的规模，其余参数由 N 确定性构造
    # 保证 M > 0，K, L 为与 N 同数量级的整数
    N = float(n)
    M = max(1, n // 10)  # 至少为 1，避免除零
    K = n // 3
    L = n // 5

    # 原逻辑使用浮点除法 N / M
    max_curr = N / M

    if M * max_curr - K < L:
        # 与原程序一致，输出 -1 并结束
        # print("-1")
        pass
        return

    def solve(curr):
        return curr * M - K >= L

    l = 0.0
    r = max_curr
    # 与原程序保持相同的二分条件与更新方式
    while r - l > 1:
        mid = (r + l) / 2
        if solve(mid):
            r = mid

        else:
            l = mid

    # print(r)
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 的大小做时间复杂度实验
    main(10**6)