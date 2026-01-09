def main(n):
    # Generate deterministic input: a[2..n] with values in [1, n]
    # For example: a[i] = (i % n) + 1
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)

    for i in range(2, n + 1):
        a[i] = (i % n) + 1
        b[a[i]] += 1

    for i in range(1, n + 1):
        if b[i] == 0:
            if 1 <= a[i] <= n:
                c[a[i]] += 1

    for i in range(1, n + 1):
        if b[i] != 0 and c[i] < 3:
            # print("NO")
            pass
            return
    # print("YES")
    pass
if __name__ == "__main__":
    main(10)