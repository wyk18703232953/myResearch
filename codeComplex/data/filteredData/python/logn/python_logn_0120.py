def solve(n, k):
    if n == 1:
        return 0

    if n <= k:
        return 1

    lo, hi = 1, k - 1
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2

        cum = (k - 2 + mid - 1) * (k - mid) // 2
        if cum < n - k:
            hi = mid - 1

        else:
            lo = mid

    if lo == 1:
        return -1

    return k - lo + 1


def main(n):
    # 将 n 作为问题规模，构造 (n, k)：
    # 令 k = max(2, n//2 + 1)，保证 k 与 n 同级别增长
    if n < 2:
        n_val = 1
        k_val = 1

    else:
        n_val = n
        k_val = max(2, n // 2 + 1)

    ans = solve(n_val, k_val)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要调整 n 的大小进行规模化实验
    main(10)