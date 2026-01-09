def main(n):
    # Deterministically generate initial s based on n
    s = n * (n + 1) // 2 + n * n

    nn = n
    ss = s
    ans = 0
    while ss > 0 and nn > 0:
        a = ss // nn
        ss -= nn * a
        ans += a
        nn -= 1
    return ans

if __name__ == "__main__":
    # print(main(10))
    pass