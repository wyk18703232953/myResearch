def main(n):
    # 映射：给定规模 n，构造一对 (N, K)
    # 这里令 N = n，K = max(1, min(n, 10^6))，保证可规模化且确定
    N = n
    K = n if n > 0 else 1

    if N == 1:
        # print(0)
        pass
    elif K + (K - 1) * (K - 2) // 2 < N:
        # print(-1)
        pass

    else:
        l = 0
        r = K - 1
        while r - l > 1:
            m = (l + r) // 2
            if (2 * K - m + 1) * m // 2 - (m - 1) >= N:
                r = m

            else:
                l = m
        # print(r)
        pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 以做规模实验
    main(10)