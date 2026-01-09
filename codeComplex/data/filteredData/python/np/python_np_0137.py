def main(n):
    # 示例：根据 n 生成 m，可按需要调整
    # 这里设定 m 为所有 p 的一半和（保证规模随 n 变化）
    p = [1 << i for i in range(n - 2, -1, -1)] + [1]
    total_p = sum(p)
    m = total_p // 2 if total_p > 0 else 0

    ans = []
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

    # print(' '.join(map(str, ans + sorted(all_nums)[::-1])))
    pass
if __name__ == "__main__":
    # 示例调用：可以修改这里的 n 以测试不同规模
    main(5)