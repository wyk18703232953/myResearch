def main(n):
    # Ensure n is at least 1 to avoid empty strings
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministically construct strings a and b based on n
    # Let len(a) = n, len(b) = 2n so the original algorithm has meaningful work
    la = n
    lb = 2 * n

    # a: alternating '1' and '0', starting with '1'
    a = ''.join('1' if i % 2 == 0 else '0' for i in range(la))
    # b: repeating pattern "101" truncated to length lb
    pattern = "101"
    b = ''.join(pattern[i % 3] for i in range(lb))

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
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)