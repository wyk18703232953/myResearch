def main(n):
    # 映射：输入规模 n -> 原程序中的 n, m
    # 这里令原始 n = n，m = n//2 + 1（保证 m > 0，且随规模变化）
    orig_n = n
    orig_m = n // 2 + 1
    a = 0
    while orig_m:
        a += orig_n // orig_m
        orig_n, orig_m = orig_m, orig_n % orig_m
    # print(a)
    pass
if __name__ == "__main__":
    main(10)