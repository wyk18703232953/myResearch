def main(n):
    # Generate deterministic input string and integer b based on n
    # String s: digits created by repeating the pattern '9876543210'
    # Length of s is n (or 1 if n = 0, to avoid empty input edge case)
    length = max(1, n)
    base_pattern = "9876543210"
    s = (base_pattern * ((length // len(base_pattern)) + 1))[:length]
    # b is a deterministic large integer derived from n
    b = int("9" * ((n % 10) + 1))

    a = ''.join(reversed(sorted(s)))
    r = ''
    while len(a) > 0:
        for i in range(len(a)):
            candidate = r + a[i] + ''.join(sorted(a[:i] + a[i + 1:]))
            if int(candidate) <= b:
                r += a[i]
                a = a[:i] + a[i + 1:]
                break
    # print(r)
    pass
if __name__ == "__main__":
    main(10)