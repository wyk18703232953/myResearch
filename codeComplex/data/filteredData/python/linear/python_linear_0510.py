def main(n):
    # Generate deterministic strings a and b of length n
    # Pattern: cycle through 'abc' and shifted version for b
    letters = ['a', 'b', 'c']
    a = ''.join(letters[i % 3] for i in range(n))
    b = ''.join(letters[(i + 1) % 3] for i in range(n))

    c = [10**10 for _ in range(n + 10)]

    if n > 0:
        c[0] = 0 if a[0] == b[0] else 1

    for i in range(1, n):
        if a[i] == b[i]:
            c[i] = c[i - 1]
        elif a[i] == b[i - 1] and a[i - 1] == b[i]:
            c[i] = (1 + c[i - 2] if i > 1 else 1)
        c[i] = min(c[i], c[i - 1] + 1)

    if n == 0:
        result = 0

    else:
        result = c[n - 1]
    # print(result)
    pass
if __name__ == "__main__":
    main(10)