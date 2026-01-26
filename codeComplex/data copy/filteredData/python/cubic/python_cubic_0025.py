def main(n):
    # Deterministically generate a string s of length n
    # Pattern: periodic with small variations via modular arithmetic
    s = []
    for i in range(n):
        # generate a lowercase letter based on i
        ch = chr(ord('a') + (i * 3 + i // 2) % 26)
        s.append(ch)
    s = "".join(s)

    leng = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if s.count(sub) >= 2 and len(sub) > leng:
                leng = len(sub)
            elif s.count(sub) == 1:
                for k in range(1, len(sub)):
                    if i - k >= 0 and s[i - k:j - k] == sub and len(sub) > leng:
                        leng = len(sub)
    # print(leng)
    pass
if __name__ == "__main__":
    main(1000)