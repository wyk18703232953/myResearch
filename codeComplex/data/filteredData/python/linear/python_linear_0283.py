def main(n):
    from collections import defaultdict

    # Deterministic generation of n strings of parentheses
    # Mix of balanced, left-heavy, right-heavy, and random-looking but deterministic patterns
    S = []
    for i in range(n):
        # Length grows roughly with n to make it scalable
        length = (i % 7 + 1) * (n // 10 + 1)
        chars = []
        for j in range(length):
            # Deterministic pattern based on i and j
            if (i + j) % 3 == 0:
                chars.append('(')
            elif (i * 2 + j) % 5 == 0:
                chars.append(')')

            else:
                # Alternate to get some balance
                chars.append('(' if j % 2 == 0 else ')')
        S.append(''.join(chars))

    d1 = defaultdict(lambda: 0)
    d2 = defaultdict(lambda: 0)
    ans = 0
    for s in S:
        cum1 = 0
        flag1 = True
        for c in s:
            if c == '(':
                cum1 += 1

            else:
                cum1 -= 1
            if cum1 < 0:
                flag1 = False
        if flag1:
            ans += d2[cum1]
        cum2 = 0
        flag2 = True
        for i in reversed(range(len(s))):
            c = s[i]
            if c == ')':
                cum2 += 1

            else:
                cum2 -= 1
            if cum2 < 0:
                flag2 = False
        if flag2:
            ans += d1[cum2]
        if cum1 == 0 and cum2 == 0 and flag1 and flag2:
            ans += 1
        if flag1:
            d1[cum1] += 1
        if flag2:
            d2[cum2] += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)