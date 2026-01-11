def main(n):
    # n 表示集合中元素数量
    # 确定性生成：使用等差序列并引入一些 2 的幂间隔，保证覆盖多种情况
    # arr 元素：从 1 开始的连续整数，再加上一些特定偏移
    base = list(range(1, n + 1))
    extra = []
    # 添加若干形如 i + 2^k 的元素（不与 base 冲突时）
    for i in range(1, min(n, 50) + 1):
        for k in range(1, 6):
            val = i + (1 << k)
            if val > n and val <= 2 * n:
                extra.append(val)
    arr = set(base + extra)

    def solve():
        for i in arr:
            for k in range(31):
                if i - (1 << k) in arr and i + (1 << k) in arr:
                    return [i - (1 << k), i, i + (1 << k)]
        for i in arr:
            for k in range(31):
                if i + (1 << k) in arr:
                    return [i, i + (1 << k)]
        for i in arr:
            return [i]

    lst = solve()
    # print(len(lst))
    pass
    # print(*lst)
    pass
if __name__ == "__main__":
    main(10)