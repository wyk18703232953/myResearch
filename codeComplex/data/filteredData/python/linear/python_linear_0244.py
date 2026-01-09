def ct(s):
    a = [0] * 52
    for ch in s:
        o = ord(ch)
        if o < 97:  # 'A'-'Z'
            a[o - 65] += 1
        else:       # 'a'-'z'
            a[o - 97 + 26] += 1
    return max(a)

def generate_string(length, shift):
    # Deterministically generate a mixed-case alphabetic string of given length
    chars = []
    for i in range(length):
        if i % 2 == 0:
            # Uppercase cycle
            c = chr(65 + (i + shift) % 26)

        else:
            # Lowercase cycle
            c = chr(97 + (i + 2 * shift) % 26)
        chars.append(c)
    return "".join(chars)

def main(n):
    # n controls both "n" in original program and the length of the base string
    # Ensure positive size
    if n <= 0:
        n = 1

    ln = n  # length of the strings
    s1_str = generate_string(ln, 1)
    s2_str = generate_string(ln, 3)
    s3_str = generate_string(ln, 5)

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

    s1, s2, s3 = s[0], s[1], s[2]
    s_sorted = sorted(s)
    if s_sorted[2] == s_sorted[1]:
        # print('Draw')
        pass
    elif s_sorted[-1] == s1:
        # print('Kuro')
        pass
    elif s_sorted[-1] == s2:
        # print('Shiro')
        pass
    elif s_sorted[-1] == s3:
        # print('Katie')
        pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(1000)