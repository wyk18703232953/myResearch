def main(n):
    # 将 n 映射为原程序中的 n, m
    # 约束：n > 0，m >= 0 并且按规模线性增长
    orig_n = max(1, n)
    orig_m = n * (n + 1) // 2  # 确定性构造，与规模 n 相关

    ans = orig_m // orig_n + min(1, orig_m % orig_n)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)