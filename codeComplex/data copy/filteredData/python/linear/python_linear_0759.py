def main(n):
    # Ensure n is non-negative
    if n < 0:
        n = 0

    # Deterministically generate input array a of length n
    # Example pattern: a[i] = i * (-1) ** i to mix positive and negative values
    a = [i if i % 2 == 0 else -i for i in range(n)]

    max_mod = 0
    max_i = -1
    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1
        if -a[i] > max_mod:
            max_mod = -a[i]
            max_i = i

    if n % 2 == 1 and max_i != -1:
        a[max_i] = -a[max_i] - 1

    # print(' '.join(map(str, a)))
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)