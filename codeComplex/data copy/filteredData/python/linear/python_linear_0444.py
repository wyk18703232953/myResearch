import sys, string

def main(n):
    # n controls the length of s and t
    # s: pattern with one '*', t: constructed to sometimes match
    if n < 2:
        n = 2
    # build s with a single '*' at position n//2
    star_pos = n // 2
    s_chars = []
    for i in range(n):
        if i == star_pos:
            s_chars.append('*')

        else:
            s_chars.append(chr(ord('a') + (i % 3)))
    s = s_chars

    # construct t deterministically based on n
    # let t length m be n + (n % 3) for variety, but ensure m >= n-1 often
    m = n + (n % 3)
    t = []
    for i in range(m):
        # mirror s around star where possible, otherwise use a fixed pattern
        if i < star_pos:
            t.append(s[i])
        elif i >= m - (n - star_pos - 1):
            # map right side of s to the end of t
            offset = (n - 1) - (m - 1 - i)
            if 0 <= offset < n and offset != star_pos:
                t.append(s[offset])

            else:
                t.append(chr(ord('b') + (i % 3)))

        else:
            t.append(chr(ord('c') + (i % 3)))

    idx = -1
    for i in range(n):
        if s[i] == '*':
            idx = i
    if idx == -1:
        if s == t:
            # print('YES')
            pass

        else:
            # print('NO')
            pass

    else:
        if m < n - 1:
            # print('NO')
            pass

        else:
            s_left = s[0:idx]
            s_right = s[idx + 1:n]
            a = len(s_left)
            b = len(s_right)
            t_left = []
            t_right = []
            for i in range(a):
                t_left.append(t[i])
                t[i] = ''
            for i in range(b):
                t_right.append(t[m - i - 1])
            if s_left == t_left and s_right == t_right[::-1]:
                # print('YES')
                pass

            else:
                # print('NO')
                pass
if __name__ == "__main__":
    # example deterministic call
    main(10)