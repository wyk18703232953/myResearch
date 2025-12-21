def main(n):
    import random
    T = n * 10
    a = []
    for idx in range(1, n + 1):
        i = random.randint(1, n)
        j = random.randint(1, T)
        a.append((idx, i, j))
    a = sorted(a, key=lambda x: x[-1])
    be, en, ans = 0, n, []
    while be < en:
        md, time, c = (be + en + 1) >> 1, 0, 0
        for _, i, j in a:
            if time + j <= T and i >= md:
                time += j
                c += 1
        if c >= md:
            be = md
        else:
            en = md - 1
    l = be
    for _, i, j in a:
        if be and i >= l:
            ans.append(_)
            be -= 1
    print(f"{l}\n{l}")
    if ans:
        print(*ans)
    return l, ans

if __name__ == "__main__":
    main(10)