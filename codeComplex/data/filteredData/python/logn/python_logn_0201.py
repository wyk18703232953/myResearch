def main(n):
    # Deterministically generate s based on n
    # Example: s cycles in a small range but fully determined by n
    s = (n // 2) % 1000 + 1

    sol = 0
    l = 1
    r = n
    while l <= r:
        sum_digits = 0
        i = (l + r) // 2
        a = i
        while a > 0:
            sum_digits += a % 10
            a = a // 10

        if i - sum_digits >= s:
            sol = n - i + 1
            r = i - 1

        else:
            l = i + 1

    return sol


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    result = main(10**6)
    # print(result)
    pass