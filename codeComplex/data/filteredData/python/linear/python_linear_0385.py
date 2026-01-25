def main(n):
    # n: problem size, mapped to original parameter n
    # m: number of (x, d) pairs, deterministically derived from n
    if n <= 0:
        return 0.0

    m = n  # scale m linearly with n

    posf = (n * (n - 1)) // 2
    if n % 2 != 0:
        negf = (n // 2) * (n // 2 + 1)
    else:
        negf = (n // 2) * (n // 2 - 1) + n // 2

    ans = 0
    for i in range(m):
        # Deterministic generation of (x, d) based on i and n
        x = i - n // 2
        d = (i % 3) - 1  # cycles through -1, 0, 1

        ans += n * x
        if d >= 0:
            ans += posf * d
        else:
            ans += negf * d

    result = ans / n
    print(result)
    return result


if __name__ == "__main__":
    # Example deterministic call
    main(10)