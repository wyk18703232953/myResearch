def main(n):
    if n < 3:
        print(-1)
        return

    # Deterministic generation of ls1 and ls2 based on n
    ls1 = [i % 10 for i in range(n)]
    ls2 = [i // 2 + 1 for i in range(n)]

    ans = float('inf')

    for i in range(1, n - 1):
        l = [ls2[j] for j in range(0, i) if ls1[j] < ls1[i]]
        r = [ls2[j] for j in range(i + 1, n) if ls1[j] > ls1[i]]

        if len(l) and len(r):
            ans = min(ans, min(l) + min(r) + ls2[i])

    print([-1, ans][ans != float('inf')])


if __name__ == "__main__":
    main(10)