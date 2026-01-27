import math

def main(n):
    # 生成确定性的 n, m, k, l
    # n 作为规模参数使用，其余参数由 n 推导，保证：
    # 1 <= m <= n
    # 0 <= k, l <= n
    if n <= 0:
        # print(-1)
        pass
        return

    N = n
    m = max(1, n // 3)
    k = n // 2
    l = n // 4

    t = int(k + l + m - 1) // m

    if k + l > N:
        # print(-1)
        pass
        return

    if m * t > N:
        # print(-1)
        pass
        return

    # print(t)
    pass
if __name__ == "__main__":
    main(10)