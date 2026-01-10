def main(n):
    # Generate a deterministic permutation of 1..n by cyclic shift
    # w will be a list of length n with elements 1..n in a fixed pattern
    if n <= 0:
        return
    shift = n // 2
    w = [((i + shift) % n) + 1 for i in range(n)]

    c = {w[j]: j + 1 for j in range(n)}
    res = 0
    for j in range(1, n + 1):
        if w[j - 1] == j:
            continue
        else:
            res += 1
            y = w[j - 1]
            w[j - 1] = j
            w[c[j] - 1] = y
            r = c[j]
            c[j] = j
            c[y] = r

    if n % 2 == 0:
        if res % 2 == 0:
            print("Petr")
        else:
            print("Um_nik")
    else:
        if res % 2:
            print("Petr")
        else:
            print("Um_nik")


if __name__ == "__main__":
    main(10)