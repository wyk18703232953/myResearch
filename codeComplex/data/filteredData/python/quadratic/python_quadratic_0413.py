def main(n):
    # Interpret n as the string length; choose k deterministically from n
    if n <= 0:
        print("")
        return

    kk = n // 2 + 1  # deterministic mapping from n to kk (number of repetitions)

    # Deterministically generate a string s of length n over lowercase letters
    # Example pattern: periodic sequence over 'a'..'z'
    base = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = "".join(base)

    # Core logic (unchanged except for removal of input)
    if (s == s[::-1] or s != s[::-1]):
        k = ""
        l = 0
        for i in reversed(range(1, n)):
            k = s[i] + k
            if s.startswith(k):
                l = len(k)
        ss = s[l:]
        fs = s + (ss * (kk - 1))
        print(fs)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)