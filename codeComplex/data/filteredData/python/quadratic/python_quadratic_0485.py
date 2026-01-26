def main(n):
    # n: size of the arrays l and r
    if n <= 0:
        return

    # Deterministic data generation for l and r based on n
    # Example pattern:
    # l[i] cycles within [0, n//2], r[i] mirrors from the end with a modular pattern
    l = [(i * 2) % (n // 2 + 1 if n // 2 + 1 > 0 else 1) for i in range(n)]
    r = [((n - 1 - i) * 3) % (n // 2 + 1 if n // 2 + 1 > 0 else 1) for i in range(n)]

    maxx = 0
    s = []
    it = 0
    for i in range(n):
        s.append(l[i] + r[i])
        if l[i] > i or r[i] > n - i - 1:
            it = 1
    its = list(s)
    while maxx < n:
        summ = 0
        ll = 0
        rr = its.count(-1)
        for i in range(n):
            if its[i] == -1:
                ll += 1
                rr -= 1
            if its[i] != -1 and i < n - 1 and r[i] < rr:
                it = 1
                break
            if its[i] != -1 and i > 0 and l[i] < ll:
                it = 1
                break
        if it == 1:
            break
        for i in range(n):
            if s[i] == maxx:
                s[i] = -maxx
                its[i] = -1
                summ += 1

        if summ == 0:
            it = 1
            break
        maxx += summ
    if it == 1:
        # print('NO')
        pass

    else:
        # print('YES')
        pass
        min_s = min(s)
        for i in s:
            # print(i - min_s + 1, end=' ')
            pass
        # print()
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)