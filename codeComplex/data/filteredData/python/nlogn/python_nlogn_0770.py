def main(n):
    MOD = 10**9 + 7

    # Deterministically generate t test cases based on n
    # Here we choose t = n, and for each test i generate an array of length i+2
    t = n

    for case_idx in range(1, t + 1):
        # Define size of this test case
        cur_n = case_idx + 2  # ensure n >= 3 generally, first is 3, then 4, ...

        # Generate array a of length cur_n deterministically
        # a[i] = (i * 2 + case_idx) % (2*cur_n + 3)
        a = [(i * 2 + case_idx) % (2 * cur_n + 3) for i in range(cur_n)]

        a.sort()

        if cur_n == 2:
            print(0)
        else:
            print(min(cur_n - 2, a[-2] - 1))


if __name__ == "__main__":
    main(5)