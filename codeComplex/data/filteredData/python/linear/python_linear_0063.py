def main(n):
    # Generate deterministic strings s and t of length n over 'a'..'z'
    # Pattern ensures a mix of equal and different positions.
    letters = [chr(ord('a') + i) for i in range(26)]
    s_list = [letters[i % 26] for i in range(n)]
    t_list = [letters[(i * 7 + 3) % 26] for i in range(n)]
    s = "".join(s_list)
    t = "".join(t_list)

    pair2ind = {}
    letters_s = [0] * 26
    letters_t = [0] * 26
    non_common = set()
    cnt = 0
    for i in range(n):
        if s[i] != t[i]:
            pair2ind[(s[i], t[i])] = i + 1
            letters_s[ord(s[i]) - ord('a')] = i + 1
            letters_t[ord(t[i]) - ord('a')] = i + 1
            non_common.add(i + 1)
            cnt += 1

    sim = -1
    for i in range(26):
        if letters_s[i] != 0 and letters_t[i] != 0:
            sim = letters_s[i]
            break

    else:
        # print(cnt)
        pass
        # print(-1, -1)
        pass
        return

    for i in range(n):
        if s[i] != t[i]:
            if (t[i], s[i]) in pair2ind:
                # print(cnt - 2)
                pass
                # print(pair2ind[(s[i], t[i])], pair2ind[(t[i], s[i])])
                pass
                return

    non_common.remove(sim)
    # print(cnt - 1)
    pass
    # print(sim, letters_t[ord(s[sim-1]) - ord('a')])
    pass
if __name__ == "__main__":
    main(10)