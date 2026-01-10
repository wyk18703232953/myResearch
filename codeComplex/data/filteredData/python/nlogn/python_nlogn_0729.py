def main(n):
    # Generate deterministic inputs a, b, c based on n
    # Use cycles of numbers 1-9 and suits 'p', 's', 'm'
    nums = [(n % 9) + 1, ((n // 3) % 9) + 1, ((n // 9) % 9) + 1]
    suits = ['p', 's', 'm']
    a = str(nums[0]) + suits[n % 3]
    b = str(nums[1]) + suits[(n + 1) % 3]
    c = str(nums[2]) + suits[(n + 2) % 3]

    s = []
    p = []
    m = []

    if a[1] == 'p':
        p.append(int(a[0]))
    elif a[1] == 's':
        s.append(int(a[0]))
    else:
        m.append(int(a[0]))

    if b[1] == 'p':
        p.append(int(b[0]))
    elif b[1] == 's':
        s.append(int(b[0]))
    else:
        m.append(int(b[0]))

    if c[1] == 'p':
        p.append(int(c[0]))
    elif c[1] == 's':
        s.append(int(c[0]))
    else:
        m.append(int(c[0]))

    s.sort()
    p.sort()
    m.sort()

    cur = 2
    if len(s) == 3:
        if s[0] == s[1] and s[1] == s[2]:
            cur = 0
        elif s[0] == s[1] or s[1] == s[2]:
            cur = 1
        else:
            if s[0] + 1 == s[1] and s[1] + 1 == s[2]:
                cur = 0
            elif s[0] + 1 == s[1] or s[1] + 1 == s[2]:
                cur = 1
            elif s[0] + 2 == s[1] or s[1] + 2 == s[2]:
                cur = 1
            else:
                cur = 2
    elif len(s) == 2:
        if s[0] == s[1]:
            cur = 1
        elif s[0] + 1 == s[1]:
            cur = 1
        elif s[0] + 2 == s[1]:
            cur = 1
        else:
            cur = 2
    else:
        cur = 2

    x = 2
    if len(p) == 3:
        if p[0] == p[1] and p[1] == p[2]:
            x = 0
        elif p[0] == p[1] or p[1] == p[2]:
            x = 1
        else:
            if p[0] + 1 == p[1] and p[1] + 1 == p[2]:
                x = 0
            elif p[0] + 1 == p[1] or p[1] + 1 == p[2]:
                x = 1
            elif p[0] + 2 == p[1] or p[1] + 2 == p[2]:
                x = 1
            else:
                x = 2
    elif len(p) == 2:
        if p[0] == p[1]:
            x = 1
        elif p[0] + 1 == p[1]:
            x = 1
        elif p[0] + 2 == p[1]:
            x = 1
        else:
            x = 2
    else:
        x = 2

    y = 2
    if len(m) == 3:
        if m[0] == m[1] and m[1] == m[2]:
            y = 0
        elif m[0] == m[1] or m[1] == m[2]:
            y = 1
        else:
            if m[0] + 1 == m[1] and m[1] + 1 == m[2]:
                y = 0
            elif m[0] + 1 == m[1] or m[1] + 1 == m[2]:
                y = 1
            elif m[0] + 2 == m[1] or m[1] + 2 == m[2]:
                y = 1
            else:
                y = 2
    elif len(m) == 2:
        if m[0] == m[1]:
            y = 1
        elif m[0] + 1 == m[1]:
            y = 1
        elif m[0] + 2 == m[1]:
            y = 1
        else:
            y = 2
    else:
        y = 2

    print(min(cur, x, y))


if __name__ == "__main__":
    main(10)