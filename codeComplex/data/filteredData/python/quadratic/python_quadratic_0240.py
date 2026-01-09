def main(n):
    # Generate deterministic test data based on n
    # Interpret n as the length of the two lists
    if n < 3:
        # print(-1)
        pass
        return

    ls1 = [i % 7 + (i // 3) for i in range(n)]
    ls2 = [(i * 2 + 3) % 10 + (i // 2) for i in range(n)]

    ans = float('inf')

    for i in range(1, n - 1):
        l = [ls2[j] for j in range(0, i) if ls1[j] < ls1[i]]
        r = [ls2[j] for j in range(i + 1, n) if ls1[j] > ls1[i]]

        if len(l) and len(r):
            ans = min(ans, min(l) + min(r) + ls2[i])

    # print([-1, ans][ans != float('inf')])
    pass
if __name__ == "__main__":
    # Example call for testing / scaling
    main(10)