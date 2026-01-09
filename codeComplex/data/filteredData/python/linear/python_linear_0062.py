def main(n):
    # Deterministic generation of s and t with length n
    # s and t use lowercase letters in a simple arithmetic pattern
    s_chars = []
    t_chars = []
    for i in range(n):
        s_chars.append(chr(ord('a') + (i % 26)))
        t_chars.append(chr(ord('a') + ((i + 1) % 26)))
    s = "".join(s_chars)
    t = "".join(t_chars)

    value = {}
    li = []
    res1 = 0
    res2 = res3 = -1

    for i in range(n):
        if s[i] != t[i]:
            value[t[i]] = i
            res1 += 1
            li.append(i)
    p = sq = False
    for i in li:
        if s[i] in value:
            p = True
            res2 = i + 1
            f = value[s[i]]
            res3 = f + 1
            if s[f] == t[i]:
                sq = True
                break

    # print(res1 - (2 if sq else 1 if p else 0))
    pass
    # print(res2, res3)
    pass
if __name__ == "__main__":
    main(10)