def main(n):
    # 解释输入结构：
    # 原程序读取：n, pos, l, r
    # 这里使用 n 作为“原来的 n”，并根据 n 确定性地构造 pos, l, r
    #
    # 规模含义：
    # - n: 原问题中的最大位置
    # - pos: 当前所在位置（1..n）
    # - l, r: 区间边界（1 <= l <= r <= n）
    #
    # 构造方式（完全确定性、可规模化）：
    # pos = n // 2 + 1
    # l = max(1, n // 3)
    # r = min(n, 2 * n // 3 + 1)
    # 保证 1 <= l <= r <= n
    if n <= 0:
        return

    nn = n
    pos = nn // 2 + 1
    l = nn // 3
    if l < 1:
        l = 1
    r = 2 * nn // 3 + 1
    if r > nn:
        r = nn
    if l > r:
        l, r = r, l

    # 保证 pos 在 [1, n]
    if pos < 1:
        pos = 1
    if pos > nn:
        pos = nn

    # 原始核心逻辑
    if l == 1 and r == nn:
        ans = 0
    elif l == 1:
        if pos == r:
            ans = 1
        elif pos > r:
            ans = pos - r + 1
        elif pos < r:
            ans = r - pos + 1
    elif r == nn:
        if pos == l:
            ans = 1
        elif pos < l:
            ans = l - pos + 1

        else:
            ans = pos - l + 1

    else:
        if pos >= l and pos <= r:
            if pos - l < r - pos:
                ans = 2 + pos - l + r - l

            else:
                ans = 2 + r - l + r - pos

        else:
            if pos > r:
                ans = pos - r + 2 + r - l

            else:
                ans = l - pos + 2 + r - l

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：对若干规模运行以便做时间复杂度实验
    for n in [1, 2, 5, 10, 100, 1000]:
        main(n)