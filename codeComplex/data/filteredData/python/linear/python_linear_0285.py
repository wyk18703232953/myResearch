def main(n):
    c, r, o, e = 0, 0, [0] * 300000, [0] * 300000

    # Deterministic generation of n parenthesis strings
    # Pattern cycles to produce various types:
    # 0: balanced, 1: more '(', 2: more ')', 3: mixed but kept simple
    for k in range(n):
        t = k % 4
        if t == 0:
            # Balanced: "() repeated"
            length = (k % 50) + 1
            s = "()" * length
        elif t == 1:
            # More '(': "(" * a + "()" * b
            a = (k % 100) + 1
            b = (k // 2 % 50)
            s = "(" * a + "()" * b
        elif t == 2:
            # More ')': "()" * b + ")" * a
            a = (k % 100) + 1
            b = (k // 3 % 50)
            s = "()" * b + ")" * a

        else:
            # Mixed but unbalanced in a controlled way
            a = (k % 70) + 1
            b = (k % 40)
            s = "(" * a + ")" * b

        l, n_unmatched = 0, 0
        for ch in s:
            if ch == '(':
                l += 1

            else:
                if l != 0:
                    l -= 1

                else:
                    n_unmatched += 1
        if l == 0 and n_unmatched == 0:
            c += 1
        elif l != 0 and n_unmatched != 0:
            pass
        elif l != 0:
            if l < 300000:
                o[l] += 1

        else:
            if n_unmatched < 300000:
                e[n_unmatched] += 1

    for i in range(300000):
        if e[i] and o[i]:
            r += e[i] * o[i]
    # print(pow(c, 2) + r)
    pass
if __name__ == "__main__":
    main(1000)