def main(n):
    from collections import Counter

    # Generate deterministic input:
    # Interpret n as the length of the array a
    # Example pattern: a[i] = (i * 3) % (2*n + 1)
    a = [(i * 3) % (2 * n + 1) for i in range(n)]

    freq = Counter(a)
    ans = 0
    for x in freq:
        for i in range(32):
            c = (1 << i) - x
            if c not in freq:
                continue
            if c == x and freq[x] == 1:
                continue
            break
        else:
            ans += freq[x]

    print(ans)


if __name__ == "__main__":
    main(10)