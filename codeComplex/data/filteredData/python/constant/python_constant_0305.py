def main(n):
    # n represents the scale of the input; construct deterministic parameters
    # Map n to k, n_val, s, p in a deterministic way
    k = max(1, n % 10 + 1)
    n_val = max(1, n)
    s = max(1, (n % 7) + 1)
    p = max(1, (n % 5) + 1)

    c = (n_val // s) if n_val % s == 0 else (n_val // s) + 1
    result = (c * k) // p if (c * k) % p == 0 else ((c * k) // p) + 1
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(1000)