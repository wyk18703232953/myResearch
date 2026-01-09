def main(n):
    # Deterministically generate k and s based on n
    # k >= 1, vary with n
    k = max(1, n // 3 + 1)
    # Build a deterministic string s of length n using cyclic letters
    alphabet = "abcd"
    s = "".join(alphabet[i % len(alphabet)] for i in range(n))

    for i in range(1, n):
        if s[:n - i] == s[i:]:
            result = s + s[n - i:] * (k - 1)
            # print(result)
            pass
            return
    # print(s * k)
    pass
if __name__ == "__main__":
    main(10)