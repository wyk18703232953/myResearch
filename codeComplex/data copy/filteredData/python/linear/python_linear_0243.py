def main(n):
    # Deterministically generate N and three strings S based on n
    # Map n to a reasonable range for N (1 to 10^6)
    N = max(1, n)

    # Generate three strings with varying patterns to exercise the logic
    # Length of each string depends on n
    length_base = max(1, n)

    # String 1: repeating pattern of 'A', length = length_base
    s1 = ''.join(chr(ord('A') + (i % 3)) for i in range(length_base))

    # String 2: alternating two characters, length = length_base + 1
    s2 = ''.join(('X' if i % 2 == 0 else 'Y') for i in range(length_base + 1))

    # String 3: periodic pattern over 4 characters, length = length_base + 2
    s3 = ''.join(chr(ord('a') + (i % 4)) for i in range(length_base + 2))

    S = [s1, s2, s3]

    bu = []
    for s in S:
        cnt = {}
        mx = 0
        for c in s:
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1
            mx = max(mx, cnt[c])
        if mx == len(s) and N == 1:
            bu.append(mx - 1)

        else:
            bu.append(min(len(s), mx + N))

    ans = -1
    ansmx = -1
    for i in range(3):
        if bu[i] > ansmx:
            ans = i
            ansmx = bu[i]
        elif bu[i] == ansmx:
            ans = -1

    if ans == -1:
        # print('Draw')
        pass
    elif ans == 0:
        # print('Kuro')
        pass
    elif ans == 1:
        # print('Shiro')
        pass

    else:
        # print('Katie')
        pass
if __name__ == "__main__":
    main(5)