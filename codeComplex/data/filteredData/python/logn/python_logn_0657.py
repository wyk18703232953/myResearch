def main(n):
    # 生成测试数据：这里随机构造一个合法的 k，
    # 做法：任选一个 mid in [0, n]，计算对应的 k
    # 然后再用原逻辑通过二分求回这个 mid。
    #
    # 如需不同的生成策略，可以按需修改。
    # 保证 k 一定有解，从而能触发 break 分支。

    # 简单选择 mid = n // 2 作为测试
    mid_true = n // 2
    k = ((n - mid_true) * (n - mid_true + 1)) // 2 - mid_true

    # 原逻辑：根据 n, k 求 mid
    l, r = 0, n
    while l < r:
        mid = (l + r) // 2
        val = ((n - mid) * (n - mid + 1)) // 2 - mid
        if val == k:
            print(mid)
            break
        elif val > k:
            l = mid
        else:
            r = mid

if __name__ == "__main__":
    # 示例调用：可按需修改 n 的测试规模
    main(10)