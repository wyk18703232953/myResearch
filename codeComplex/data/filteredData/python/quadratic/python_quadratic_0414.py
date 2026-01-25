def main(n):
    # n: length of the base string s
    if n <= 0:
        return
    # deterministically generate k and s from n
    k = n % 7 + 1
    s = "".join(chr(ord('a') + (i % 26)) for i in range(n))

    for i in range(1, n):
        if s[:n - i] == s[i:]:
            print(s + s[n - i:] * (k - 1))
            return
    print(s * k)


if __name__ == "__main__":
    main(10)