def main(n):
    # Deterministic generation of three strings a, b, c
    # Structure inferred from original code: each is "<digit><char>"
    # We map n to a pattern that cycles deterministically.
    # Digits from 1..9, suits from 'a','b','c'
    d1 = (n % 9) + 1
    d2 = ((n // 2) % 9) + 1
    d3 = ((n // 3) % 9) + 1

    s1 = chr(ord('a') + (n % 3))
    s2 = chr(ord('a') + ((n // 2) % 3))
    s3 = chr(ord('a') + ((n // 3) % 3))

    a = str(d1) + s1
    b = str(d2) + s2
    c = str(d3) + s3

    if a[1] == b[1] == c[1]:
        t = sorted([int(a[0]), int(b[0]), int(c[0])])
        if (t[1] == t[0] + 1 == t[2] - 1) or (t[0] == t[2]):
            print(0)
        elif t[0] == t[1] or t[1] == t[2]:
            print(1)
        elif (
            t[0] + 1 == t[1]
            or t[1] + 1 == t[2]
            or t[0] + 2 == t[1]
            or t[1] + 2 == t[2]
        ):
            print(1)
        else:
            print(2)
    elif a[1] == b[1]:
        s, t = int(a[0]), int(b[0])
        if s == t:
            print(1)
        elif min(s, t) + 1 == max(s, t) or min(s, t) + 2 == max(s, t):
            print(1)
        else:
            print(2)
    elif c[1] == b[1]:
        s, t = int(c[0]), int(b[0])
        if s == t:
            print(1)
        elif min(s, t) + 1 == max(s, t) or min(s, t) + 2 == max(s, t):
            print(1)
        else:
            print(2)
    elif a[1] == c[1]:
        s, t = int(a[0]), int(c[0])
        if s == t:
            print(1)
        elif min(s, t) + 1 == max(s, t) or min(s, t) + 2 == max(s, t):
            print(1)
        else:
            print(2)
    else:
        print(2)


if __name__ == "__main__":
    main(10)