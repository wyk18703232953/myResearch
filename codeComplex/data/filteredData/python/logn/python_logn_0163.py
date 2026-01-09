def main(n):
    # 映射规则：
    # N = n
    # K = n（保证规模与 n 成正比，且覆盖 K 的变化）
    N = n
    K = n

    def in_bounds(k):
        return N <= K * (K + 1) // 2 - (K - k) * (K - k + 1) // 2 - k + 1

    l = 0
    r = K
    while l <= r:
        c = (l + r) // 2
        if in_bounds(c):
            r = c - 1

        else:
            l = c + 1
    if in_bounds(K):
        # print(l)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)