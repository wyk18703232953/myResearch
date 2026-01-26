def ct(s):
    a = [0] * (26 * 2)
    for ch in s:
        o = ord(ch)
        if o < 97:
            a[o - 65] += 1

        else:
            a[o - 97 + 26] += 1
    return max(a)

def generate_string(n, offset):
    # deterministic mixed upper/lower letters, length n
    chars = []
    for i in range(n):
        if (i + offset) % 2 == 0:
            # uppercase A-Z
            chars.append(chr(65 + ((i + offset) % 26)))

        else:
            # lowercase a-z
            chars.append(chr(97 + ((i * 2 + offset) % 26)))
    return "".join(chars)

def main(n):
    if n <= 0:
        n = 1
    ln = n
    s1_str = generate_string(ln, 0)
    s2_str = generate_string(ln, 1)
    s3_str = generate_string(ln, 2)

    s1 = ct(s1_str)
    s2 = ct(s2_str)
    s3 = ct(s3_str)

    s = [s1, s2, s3]

    for i in range(3):
        if s[i] == ln and n == 1:
            s[i] = ln - 1

        else:
            s[i] = s[i] + n
        if s[i] > ln:
            s[i] = ln

    s1 = s[0]
    s2 = s[1]
    s3 = s[2]

    s_sorted = sorted(s)
    if s_sorted[2] == s_sorted[1]:
        # print("Draw")
        pass
    elif s_sorted[-1] == s1:
        # print("Kuro")
        pass
    elif s_sorted[-1] == s2:
        # print("Shiro")
        pass
    elif s_sorted[-1] == s3:
        # print("Katie")
        pass
if __name__ == "__main__":
    main(10)