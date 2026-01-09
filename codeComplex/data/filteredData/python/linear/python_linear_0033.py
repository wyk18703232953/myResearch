def main(n):
    # Deterministically generate a string s of length n using 'H' and 'T'
    # Example pattern: alternate 'H' and 'T'
    s = ''.join('H' if i % 2 == 0 else 'T' for i in range(n))

    hc = s.count('H')
    tc = s.count('T')

    if n - hc <= 0:
        hr = 0

    else:
        hr = min(s[i:i + hc].count('T') for i in range(n - hc + 1))

    if n - tc <= 0:
        tr = 0

    else:
        tr = min(s[i:i + tc].count('H') for i in range(n - tc + 1))

    result = min(hr, tr)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)