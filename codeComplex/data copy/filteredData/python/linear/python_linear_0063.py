def main(n):
    # Ensure n is at least 1 to avoid empty strings
    if n <= 0:
        return

    # Deterministic construction of s and t based on n
    # Use lowercase letters cyclically
    chars = [chr(ord('a') + i) for i in range(26)]
    s_list = [chars[i % 26] for i in range(n)]
    t_list = [chars[(i + 1) % 26] for i in range(n)]

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
    # print(sim, letters_t[ord(s[sim - 1]) - ord('a')])
    pass
    return


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)