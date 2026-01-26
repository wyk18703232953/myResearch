def main(n):
    from collections import defaultdict

    # Generate deterministic test data: n parenthesis strings
    # Here we let the i-th string have length i+1 and a simple pattern
    S = []
    for i in range(n):
        length = i + 1
        s = []
        for j in range(length):
            # Deterministic pattern depending on i and j
            if (i + j) % 2 == 0:
                s.append('(')

            else:
                s.append(')')
        S.append(''.join(s))

    d1 = defaultdict(lambda: 0)
    d2 = defaultdict(lambda: 0)
    ans = 0
    for idx, s in enumerate(S):
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

    return ans


if __name__ == "__main__":
    # Example deterministic call; change n as needed for experiments
    result = main(10)
    # print(result)
    pass