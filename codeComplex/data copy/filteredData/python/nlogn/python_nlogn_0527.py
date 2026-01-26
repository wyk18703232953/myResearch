def main(n):
    # Deterministically generate k and array a based on n
    # Ensure k >= 2 and somewhat proportional to n
    k = max(2, n // 2 + 1)

    # Generate n integers for a; values grow with i and n, but deterministically
    a = [(i * i + 3 * i + n) for i in range(1, n + 1)]

    a_pows = []
    a_pow_dict = [{} for _ in range(11)]
    for j in range(n):
        x = a[j] % k
        i = 0
        while i < 11:
            if x in a_pow_dict[i]:
                a_pow_dict[i][x] += 1

            else:
                a_pow_dict[i][x] = 1
            i += 1
            x = (x * 10) % k

    c = 0

    for x in a:
        m = len(str(x))
        if (-x) % k in a_pow_dict[m]:
            c += a_pow_dict[m][(-x) % k]
            c -= int(int(str(x) * 2) % k == 0)

    return c


if __name__ == "__main__":
    # Example call for time-complexity experiment
    result = main(1000)
    # print(result)
    pass