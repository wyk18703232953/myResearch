def main(n):
    if n < 1:
        # print("YES")
        pass
        return

    # Deterministic generation of a[2..n], values in [1, n]
    # Pattern: a[i] = i // 2 (classic parent array style, with clamp to at least 1)
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        parent = i // 2
        if parent < 1:
            parent = 1
        if parent > n:
            parent = n
        a[i] = parent

    b = [0] * (n + 1)
    c = [0] * (n + 1)

    for i in range(2, n + 1):
        b[a[i]] += 1
    for i in range(1, n + 1):
        if b[i] == 0:
            c[a[i]] += 1
    for i in range(1, n + 1):
        if b[i] != 0 and c[i] < 3:
            # print("NO")
            pass
            return
    # print("YES")
    pass
if __name__ == "__main__":
    # Example deterministic run
    main(10)