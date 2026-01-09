def main(n):
    # Interpret n as the base to deterministically construct n, m, a, b
    # Ensure m > 0
    m = n + 1
    a = n + 2
    b = n + 3
    n_val = n

    r = n_val % m
    result = min(r * b, (m - r) * a)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)