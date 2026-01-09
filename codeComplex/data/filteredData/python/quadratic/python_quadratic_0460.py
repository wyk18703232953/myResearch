def main(n):
    # Generate a permutation l of [1..n] deterministically by a simple pattern
    # l[i] = (2*i + 1) % n + 1 ensures values in [1..n], and is a permutation when n is odd.
    # For even n, this pattern may not be a permutation, but the original algorithm
    # only assumes values are in 1..n, not strictly permutation for correctness of timing.
    l = [(2 * i + 1) % n + 1 for i in range(n)]

    p = [0] * n
    for i in range(n):
        p[l[i] - 1] = i

    res = ['?'] * n

    for e in range(n, 0, -1):
        i = p[e - 1]
        res[i] = 'B'
        for j in range(i % e, n, e):
            if i != j and l[i] <= l[j] and res[j] == 'B':
                res[i] = 'A'
                break
    # print(''.join(res))
    pass
if __name__ == "__main__":
    main(10)