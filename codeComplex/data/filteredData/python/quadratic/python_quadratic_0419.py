def main(n):
    # Interpret n as the length of string s
    # Deterministic generation of k and s based on n
    if n <= 0:
        return

    # Choose k as a simple deterministic function of n to make it scale with n
    k = n // 2 + 1

    # Generate a deterministic string s of length n using lowercase letters
    # Pattern: cyclic over 'a' to 'z'
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    m = -1
    for i in range(0, n - 1):
        ff = 0
        for j in range(0, i + 1):
            if s[j] != s[n - i - 1 + j]:
                ff = 1
                break
        if ff == 0:
            m = i

    # Reproduce the original output behavior
    result = []
    result.append(s)
    for _ in range(1, k):
        for j in range(m + 1, n):
            result.append(s[j])

    output = ''.join(result)
    # print(output)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)