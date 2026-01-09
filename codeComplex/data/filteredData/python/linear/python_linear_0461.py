def main(n):
    # Deterministic data generation based on n
    # Interpret n as both the length of the string and the value of k
    k = n
    # Generate a deterministic parentheses string of length n
    s = [('(' if i % 2 == 0 else ')') for i in range(n)]
    s = list(s)

    if len(s) > k:
        p = '(' * (k // 2)
        p = list(p)
        c = 0
        for i in range(0, len(s)):
            if s[i] == ')':
                p.insert(i, ')')
                c += 1
                if c == k // 2:
                    break
        # print("".join(p))
        pass

    else:
        # print("".join(s))
        pass
if __name__ == "__main__":
    main(10)