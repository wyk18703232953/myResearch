def main(n):
    # 生成确定性测试数据：长度为 n 的整数数组
    if n <= 1:
        print(0)
        return
    nums = [i * 3 + 1 for i in range(n)]

    ans = 10 ** 12
    for idx, num in enumerate(nums):
        dist = max(idx, n - idx - 1)
        # 原代码在 idx == 0 或 idx == n-1 时 dist 可能为 0，会导致除零错误
        # 为保持可运行性，这里跳过 dist 为 0 的情况
        if dist == 0:
            continue
        curr = num // dist
        ans = min(ans, curr)
    print(ans)


if __name__ == "__main__":
    main(10)