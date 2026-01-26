casas, tubos = 0, 0

def bs(c, t):
    l, r = 0, t - 1
    while l <= r:
        mid = (l + r) >> 1
        if ((2 * t - mid - 1) * mid) // 2 + 1 < c:
            l = mid + 1

        else:
            r = mid - 1
    return r + 1

def main(n):
    global casas, tubos
    # 将 n 映射为 casas, tubos，保证规模随 n 增长
    # 这里设定 tubos = n，casas = n*(n+1)//2 的一部分，保证有意义
    tubos = n if n > 0 else 1
    casas = (n * (n + 1)) // 4 + 1
    res = bs(casas, tubos)
    # print(-1 if res == tubos else res)
    pass
if __name__ == "__main__":
    main(10)