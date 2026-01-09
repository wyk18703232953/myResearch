def main(n):
    # Deterministically generate input data based on n
    # s: strictly increasing sequence with minor pattern
    s = [i + (i % 3) for i in range(n)]
    # ce: deterministic cost pattern
    ce = [(i * 7 + 3) % 1000 + 1 for i in range(n)]

    best = 10**9
    for j in range(1, n - 1):
        a = ce[j]
        b = 10**9
        c = 10**9
        for i in range(j - 1, -1, -1):
            if s[i] < s[j]:
                if ce[i] < b:
                    b = ce[i]
        for k in range(j + 1, n):
            if s[k] > s[j]:
                if ce[k] < c:
                    c = ce[k]
        current = a + b + c
        if current < best:
            best = current

    if best >= 10**9:
        # print(-1)
        pass

    else:
        # print(best)
        pass
if __name__ == "__main__":
    main(1000)