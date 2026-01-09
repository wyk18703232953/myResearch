def main(n):
    # 将 n 映射为 N 和 K，用于可规模化且确定性的生成
    # N 和 K 至少为 1，避免除零
    N = max(1, n)
    K = max(1, n // 2 + 1)

    Rcnt = N * 2
    Gcnt = N * 5
    Bcnt = N * 8

    res = (Rcnt + K - 1) // K + (Gcnt + K - 1) // K + (Bcnt + K - 1) // K
    # print(res)
    pass
if __name__ == "__main__":
    main(10)