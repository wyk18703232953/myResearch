def main(n):
    # n is the length of the permutation a, with values 1..n
    if n <= 0:
        return

    # Deterministically construct a permutation of 1..n
    # Example scheme: odd numbers ascending, then even numbers descending
    odds = [i for i in range(1, n + 1) if i % 2 == 1]
    evens = [i for i in range(n if n % 2 == 0 else n - 1, 0, -2)]
    a = odds + evens

    n2idx = {a[i]: i for i in range(n)}

    f = [False] * (n + 1)

    for i in range(n, 0, -1):
        idx_lg = n2idx[i]

        win_flag = False
        for j in range(idx_lg % i, n, i):
            if a[j] > i and not f[a[j]]:
                win_flag = True
                break
        f[i] = win_flag

    result = ''.join(['A' if f[a_i] else 'B' for a_i in a])
    print(result, flush=True)


if __name__ == "__main__":
    # Example deterministic call for experiment
    main(10)