def main(n):
    from collections import defaultdict as dd

    mod = 10**9 + 7

    # Deterministic data generation: array a of length n
    # Example pattern: a[i] = (i % 7) + 1 to ensure divisibility structure
    a = [(i % 7) + 1 for i in range(n)]

    b = sorted(a)
    c = dd(int)

    ans = 0
    val = 0
    for i in range(n):
        if c[b[i]] == 0:
            val += 1
            for j in range(n):
                if b[j] % b[i] == 0:
                    c[b[j]] = val

    for i in c:
        ans = max(ans, c[i])

    # print(ans)
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(6)