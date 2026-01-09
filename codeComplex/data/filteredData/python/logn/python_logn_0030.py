def main(n):
    # 映射规则：
    # 将 n 映射为区间 [l, r]，使得规模随 n 线性增长：
    # l = 1, r = n + 1  (保证 r > l，当 n >= 1 时)
    l = 1
    r = max(2, n + 1)  # 确保 r > l

    def core(l, r):
        if l == r:
            return 0

        val = 1
        while val * 2 <= r:
            val *= 2

        if val <= l:
            return core(l - val, r - val)

        else:
            return 2 * val - 1

    return core(l, r)


if __name__ == "__main__":
    # 示例调用，可调整 n 以改变规模
    n = 10
    # print(main(n))
    pass