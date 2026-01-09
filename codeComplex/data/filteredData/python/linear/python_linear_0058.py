def main(n):
    # Generate deterministic strings s and t of length n
    # Alphabet: 'a'..'z'
    s_chars = []
    t_chars = []
    for i in range(n):
        # Example deterministic pattern:
        # s: repeating 'a'..'z'
        # t: shifted by 1 with an additional pattern to ensure differences
        s_char = chr(ord('a') + (i % 26))
        t_char = chr(ord('a') + ((i + 1 + (i // 3)) % 26))
        s_chars.append(s_char)
        t_chars.append(t_char)
    s = "".join(s_chars)
    t = "".join(t_chars)

    dif = {}
    hem = 0
    for i in range(n):
        if s[i] != t[i]:
            dif[i] = [s[i], t[i]]
            hem += 1

    change = []
    probed = []
    k = 0
    for i in dif.keys():
        if dif[i] in probed:
            continue
        probed.append(dif[i])
        k += 1
        for j in list(dif.keys())[k:]:
            if dif[i] == dif[j][::-1]:
                # print(hem - 2)
                pass
                # print(i + 1, j + 1)
                pass
                return
            if not change and (dif[i][0] == dif[j][1] or dif[j][0] == dif[i][1]):
                change = [i, j]

    if change:
        # print(hem - 1)
        pass
        # print(change[0] + 1, change[1] + 1)
        pass

    else:
        # print(hem)
        pass
        # print('-1 -1')
        pass
if __name__ == "__main__":
    # Example deterministic call for testing / scaling
    main(1000)