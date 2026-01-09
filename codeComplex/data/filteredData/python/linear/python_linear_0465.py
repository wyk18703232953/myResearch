def main(n):
    # Generate deterministic string of length n using a simple periodic pattern
    if n <= 0:
        # print(0)
        pass
        return
    base_chars = ['a', 'b', 'c', 'd']
    s = ''.join(base_chars[i % 4] for i in range(n))
    s = s + s

    length = len(s)
    an = 1
    m = 1
    for i in range(1, length):
        if s[i] != s[i - 1]:
            m += 1
            an = max(an, m)

        else:
            an = max(an, m)
            m = 1
    # print(min(an, length // 2))
    pass
if __name__ == "__main__":
    main(10)