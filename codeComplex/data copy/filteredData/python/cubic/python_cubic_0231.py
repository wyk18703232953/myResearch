def main(n):
    mod = 10**9 + 7

    # Map n to sizes of the three arrays
    # Simple deterministic rule: split n into three parts
    if n <= 0:
        return 0
    n_a = n
    n_b = max(1, n // 2)
    n_c = max(1, n // 3)

    # Deterministic data generation
    a = [(i * 2 + 1) % mod for i in range(n_a)]
    b = [(i * 3 + 2) % mod for i in range(n_b)]
    c = [(i * 5 + 3) % mod for i in range(n_c)]

    d = {}

    def go(i, j, k):
        val = i * 40401 + j * 201 + k
        if val in d:
            return d[val]
        ret = 0
        if i < n_a and j < n_b and k < n_c:
            ret = max(
                a[i] * b[j] + go(i + 1, j + 1, k),
                b[j] * c[k] + go(i, j + 1, k + 1),
                c[k] * a[i] + go(i + 1, j, k + 1),
            )
        elif i < n_a and j < n_b:
            ret = a[i] * b[j] + go(i + 1, j + 1, k)
        elif j < n_b and k < n_c:
            ret = b[j] * c[k] + go(i, j + 1, k + 1)
        elif k < n_c and i < n_a:
            ret = c[k] * a[i] + go(i + 1, j, k + 1)
        d[val] = ret
        return ret

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    return go(0, 0, 0)


if __name__ == "__main__":
    # Example call for deterministic experiment
    result = main(10)
    # print(result)
    pass