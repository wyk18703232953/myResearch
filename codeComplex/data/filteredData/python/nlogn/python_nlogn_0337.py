def main(n):
    # Deterministically generate n strings
    # Use increasing lengths to exercise the algorithm
    s = ['']
    for i in range(n):
        # Generate a string of length i+1 with repeated pattern "ab"
        length = i + 1
        base = "ab"
        inp = (base * ((length + 1) // 2))[:length]
        s.append(inp)
        pos = len(s) - 1
        while len(s[pos]) < len(s[pos - 1]):
            s[pos], s[pos - 1] = s[pos - 1], s[pos]
            pos -= 1
    out = 'YES'
    for i in range(n):
        if s[i] not in s[i + 1]:
            out = 'NO'
            s = []
            break
    print(out + '\n'.join(s))


if __name__ == "__main__":
    main(10)