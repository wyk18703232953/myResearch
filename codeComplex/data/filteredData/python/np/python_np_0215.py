import itertools

def main(n):
    if n < 2:
        return 0

    # Deterministic generation of parameters based on n
    l = n
    r = n * n
    x = max(1, n // 3)

    # Deterministic generation of C with size n
    C = [i * 2 + 1 for i in range(n)]

    ans = 0
    for i in range(2, n + 1):
        for c in itertools.combinations(C, i):
            d = sum(c)
            if d < l or d > r:
                continue
            if max(c) - min(c) < x:
                continue
            ans += 1

    print(ans)
    return ans

if __name__ == "__main__":
    main(10)