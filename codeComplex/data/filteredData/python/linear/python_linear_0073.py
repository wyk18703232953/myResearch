def main(n):
    # Deterministic generation of strings a and b
    # Let length of a = n, length of b = 2n (with n >= 1)
    if n <= 0:
        return 0

    # Generate a as a binary string with a simple deterministic pattern
    # a[i] = '1' if i is even else '0'
    a = ''.join('1' if i % 2 == 0 else '0' for i in range(n))

    # Generate b as another deterministic binary string of length 2n
    # b[i] = '1' if (i // 2) % 2 == 0 else '0'
    b = ''.join('1' if (i // 2) % 2 == 0 else '0' for i in range(2 * n))

    ans = 0

    ones = [0 for _ in range(len(b) + 1)]
    zeros = [0 for _ in range(len(b) + 1)]

    for i in range(len(b)):
        ones[i] = ones[i - 1] + int(b[i])
        zeros[i] = i + 1 - ones[i]

    for i in range(len(a)):
        if a[i] == '1':
            ans += zeros[len(b) - len(a) + i] - zeros[i - 1]

        else:
            ans += ones[len(b) - len(a) + i] - ones[i - 1]

    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(10)