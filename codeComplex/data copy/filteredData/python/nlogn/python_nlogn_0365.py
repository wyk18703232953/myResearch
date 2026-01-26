def main(n):
    # Interpret n as the length of the list t
    # Generate deterministic k and t
    k = n // 2 + 1  # deterministic function of n

    # Generate a deterministic non-decreasing list t of length n
    # Example pattern: t[i] = i // 2  (many duplicates, then increasing)
    t = [i // 2 for i in range(n)]

    t.sort()

    f = {}
    for j in t:
        if j not in f:
            f[j] = 1

        else:
            f[j] += 1

    p = 0
    for j in range(n):
        if j < n - 1:
            if t[j + 1] > t[j] and t[j] + k >= t[j + 1]:
                p += f[t[j]]

    # print(n - p)
    pass
if __name__ == "__main__":
    main(10)