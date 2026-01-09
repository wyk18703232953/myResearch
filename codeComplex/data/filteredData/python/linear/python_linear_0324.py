def main(n):
    from collections import Counter

    # Generate deterministic string lists of size n for a and b
    # Pattern ensures some overlaps and some differences
    a = Counter()
    b = Counter()

    # First list: strings based on i % (n//2 + 1) to create repetition
    for i in range(n):
        s = "s_" + str(i % (n // 2 + 1))
        a[s] += 1

    # Second list: slightly shifted pattern to create differences
    for i in range(n):
        s = "s_" + str((i + 1) % (n // 2 + 1))
        b[s] += 1

    ans = 0
    for key in b:
        ans += max(b[key] - a[key], 0)

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)