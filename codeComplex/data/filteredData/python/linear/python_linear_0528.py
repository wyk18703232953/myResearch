def main(n):
    # Map n to string length and k
    if n <= 0:
        return
    k = max(1, n // 5)
    if k > 26:
        k = 26
    length = n

    # Generate deterministic string s of uppercase letters A-Z
    # Pattern: s[i] = chr(ord('A') + (i % k))
    s = "".join(chr(ord('A') + (i % k)) for i in range(length))

    c = [0] * 26
    for i in range(length):
        if s[i] <= chr(ord('A') + k - 1):
            c[ord(s[i]) - ord('A')] += 1
    result = min(c[:k]) * k
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)