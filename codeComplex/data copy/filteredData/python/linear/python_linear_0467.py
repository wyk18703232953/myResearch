def main(n):
    # Deterministically generate a string of length n over 'a' and 'b'
    # to control input size; pattern repeats every 3 chars.
    if n <= 0:
        return 0
    s = [('a', 'b', 'a')[i % 3] for i in range(n)]
    s = s + s  # extend(s)
    cnt = 0
    c = 1
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            c += 1

        else:
            if c > cnt:
                cnt = c
            c = 1
    if c > cnt:
        cnt = c
    result = min(cnt, n)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)