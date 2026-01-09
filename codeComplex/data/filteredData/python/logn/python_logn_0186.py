def main(n: int):
    """
    将原程序改为可参数化规模 n 的版本。
    这里根据 n 生成测试数据：设 s = n // 2。
    原逻辑：给定 n, s，找最小的 x ∈ [s, n] 使得 x >= s + sum_digits(x)，
    若不存在则答案为 0，否则为 n - x + 1。
    """
    s = n // 2  # 根据规模 n 自动生成一个 s，用户可按需修改生成规则

    lo, hi = s, n
    ans = n + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        z = sum(map(int, str(mid)))
        if mid >= s + z:
            ans = mid
            hi = mid - 1

        else:
            lo = mid + 1

    result = max(0, n - ans + 1)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改测试规模
    main(10**6)