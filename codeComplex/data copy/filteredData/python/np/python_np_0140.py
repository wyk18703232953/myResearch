def main(n):
    # 这里根据 n 生成一个 m，用于测试。
    # 原程序中 m 的上界与 n 相关：p 是长度为 n 的数组，前 n-1 个元素为 2^(n-2)...2^0，最后一个为 1，
    # 因此前 n-1 个元素的和为 2^(n-1) - 1，最后一个 1 再加上，总和约为 2^(n-1)。
    # 为了让逻辑有意义，取一个在 [1, 2^(n-1)] 范围内的 m。
    if n <= 0:
        return ""
    # 简单地取 m = 2^(n-1) // 2，确保不为 0
    m = max(1, (1 << (n - 1)) // 2)

    ans = []
    p = [1 << i for i in range(n - 2, -1, -1)] + [1]
    all_nums = set(range(1, n + 1))
    num, cur, i = 1, 0, 0

    while i < len(p) and m > 0 and num <= n:
        cur += p[i]
        if cur >= m:
            m -= (cur - p[i])
            cur = 0
            ans.append(num)
            all_nums.discard(num)
        num += 1
        i += 1

    result = ' '.join(map(str, ans + sorted(all_nums)[::-1]))
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(5)