def main(n):
    # Deterministically generate a string of length n
    # Pattern: repeating lowercase letters 'a' to 'z'
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    n = len(s)
    m = n - 1
    while m > 0:
        f = False
        for i in range(0, n - m):
            for j in range(i + 1, n - m + 1):
                x = True
                for k in range(0, m):
                    if s[i + k] != s[j + k]:
                        x = False
                        break
                if x:
                    f = True
                    break
            if f:
                break
        if f:
            break
        m -= 1
    # print(m)
    pass
if __name__ == "__main__":
    main(1000)