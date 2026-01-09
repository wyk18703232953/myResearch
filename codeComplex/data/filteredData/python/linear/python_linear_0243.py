def main(n):
    # Deterministically generate N based on n
    # Ensure N >= 1
    N = max(1, n)

    # Deterministically generate 3 strings S[0], S[1], S[2] of length n
    # Use simple patterns to scale with n
    letters = "abcdefghijklmnopqrstuvwxyz"
    L = len(letters)

    # S[0]: repeating alphabet pattern
    s0 = "".join(letters[i % L] for i in range(n))

    # S[1]: reversed alphabet pattern
    s1 = "".join(letters[(L - 1 - (i % L))] for i in range(n))

    # S[2]: alternating between two characters plus index-based shift
    s2 = "".join(letters[(i * 2) % L] for i in range(n))

    S = [s0, s1, s2]

    bu = []
    for s in S:
        cnt = {}
        mx = 0
        for c in s:
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1
            if cnt[c] > mx:
                mx = cnt[c]
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
    # Example call for time complexity experiments
    main(10)