def main(n):
    # Generate deterministic string s of length n over lowercase letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    L = len(alphabet)
    s = [alphabet[i % L] for i in range(n)]

    if len(set(s)) == len(s):
        # print('0')
        pass
        return

    d = []

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            x = ''
            for k in range(i, j + 1):
                x += s[k]
            d.append(x)

    v = {}
    for i in range(len(s)):
        if s[i] not in v:
            v[s[i]] = 1

        else:
            v[s[i]] += 1

    for i in d:
        if i not in v:
            v[i] = 1

        else:
            v[i] += 1

    mx = -1

    for i in v:
        if v[i] >= 2:
            if len(i) > mx:
                mx = max(mx, len(i))

    # print(mx)
    pass
if __name__ == "__main__":
    main(10)