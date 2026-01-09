from collections import Counter

def main(n):
    # Interpret n as both: string length and allowed changes
    # Generate three deterministic strings of length n
    a = ''.join(chr(ord('a') + (i % 3)) for i in range(n))
    b = ''.join(chr(ord('b') + (i % 3)) for i in range(n))
    c = ''.join(chr(ord('c') + (i % 3)) for i in range(n))

    fa = Counter(a)
    fb = Counter(b)
    fc = Counter(c)

    la = min(fa.most_common(1)[0][1] + n, len(a))
    lb = min(fb.most_common(1)[0][1] + n, len(b))
    lc = min(fc.most_common(1)[0][1] + n, len(c))

    if fa.most_common(1)[0][1] == len(a) and n == 1:
        la = len(a) - 1

    if fb.most_common(1)[0][1] == len(b) and n == 1:
        lb = len(b) - 1

    if fc.most_common(1)[0][1] == len(c) and n == 1:
        lc = len(c) - 1

    if la > max(lb, lc):
        # print("Kuro")
        pass
    elif lb > max(la, lc):
        # print("Shiro")
        pass
    elif lc > max(la, lb):
        # print("Katie")
        pass

    else:
        # print("Draw")
        pass
if __name__ == "__main__":
    main(10)