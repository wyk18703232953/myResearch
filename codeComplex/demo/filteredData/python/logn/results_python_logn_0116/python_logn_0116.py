def main(n):
    # Interpret n as the magnitude of l and r.
    # Deterministically generate l and r such that l <= r and they are not always equal.
    # Example: l = n, r = 2*n + (n // 2)
    l = n
    r = 2 * n + (n // 2)

    if l > r:
        l, r = r, l

    ans = 0
    if l == r:
        return 0

    for i in range(63, -1, -1):
        if (r ^ l) & (1 << i):
            for j in range(i, -1, -1):
                ans |= 1 << j
            break
    return ans


if __name__ == "__main__":
    # Example call for testing and time complexity experiments
    result = main(10**6)
    # print(result)
    pass