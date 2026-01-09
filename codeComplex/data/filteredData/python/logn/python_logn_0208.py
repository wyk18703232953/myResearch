def main(n):
    # 确定性生成 s，映射为与 n 规模相关的整数
    s = n // 2 + 1
    lo = 0
    hi = n
    ans = n + 1
    while lo <= hi:
        mi = (lo + hi) >> 1
        curr = sum(int(i) for i in str(mi))
        if mi - curr >= s:
            hi = mi - 1
            ans = mi

        else:
            lo = mi + 1
    # print(n - ans + 1)
    pass
if __name__ == "__main__":
    main(10**6)