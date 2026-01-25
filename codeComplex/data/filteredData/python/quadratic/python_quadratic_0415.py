def main(n):
    # n controls the length of the base string s and also the magnitude of k
    if n <= 0:
        return

    # Deterministically construct s: repeat 'abc' pattern up to length n
    base_pattern = "abc"
    s = (base_pattern * ((n + len(base_pattern) - 1) // len(base_pattern)))[:n]

    # Deterministically define k as a function of n (at least 1)
    k = n // 3 + 1

    fail = [-1] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        j = fail[i - 1]
        while j != -1 and s[i - 1] != s[j]:
            j = fail[j]
        fail[i] = j + 1

    f1 = fail[-1]
    result = s + s[f1:] * (k - 1)
    print(result)


if __name__ == "__main__":
    main(10)