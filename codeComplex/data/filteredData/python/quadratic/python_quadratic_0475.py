def main(n):
    # Deterministic data generation for time complexity experiments
    # Define l and r based on n and indices to keep them small and valid-ish
    l = [i % 3 for i in range(n)]
    r = [(n - 1 - i) % 3 for i in range(n)]

    res = [0] * n
    for i in range(n):
        res[i] = n - l[i] - r[i]
    for i in range(n):
        ok = 0
        for j in range(i):
            if res[j] > res[i]:
                ok += 1
        if ok != l[i]:
            # print("NO")
            pass
            return
        ok = 0
        for j in range(i + 1, n):
            if res[j] > res[i]:
                ok += 1
        if ok != r[i]:
            # print("NO")
            pass
            return
    # print("YES")
    pass
    # print(' '.join(map(str, res)))
    pass
if __name__ == "__main__":
    main(10)