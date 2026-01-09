def main(n):
    # Ensure n is at least 3 because the original loop runs from 1 to n-2
    if n < 3:
        # print(-1)
        pass
        return

    # Deterministic generation of a and b based on n
    # a: strictly increasing sequence to allow many valid triples
    a = [i for i in range(1, n + 1)]
    # b: some varying costs, deterministic pattern
    b = [(i * 3) % 10 + (i // 3) for i in range(n)]

    ans = float('inf')
    for i in range(1, n - 1):
        bef = aft = float('inf')
        for j in range(i):
            if a[j] < a[i]:
                bef = min(bef, b[j])
        for j in range(i, n):
            if a[i] < a[j]:
                aft = min(aft, b[j])
        ans = min(ans, b[i] + bef + aft)
    # print(-1 if ans > 10 ** 9 else ans)
    pass
if __name__ == "__main__":
    main(1000)