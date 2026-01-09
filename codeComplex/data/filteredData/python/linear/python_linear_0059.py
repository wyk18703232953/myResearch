def main(n):
    # Ensure n is at least 1 to avoid empty strings
    if n <= 0:
        return

    # Deterministic generation of s and t of length n over 'a'..'z'
    # s: repeating alphabet
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    # t: s shifted by 1 position in alphabet (cyclic), to guarantee some differences
    t = ''.join(chr(ord('a') + ((i + 1) % 26)) for i in range(n))

    p = [-1, -1]
    a = [[-1] * 26 for _ in range(26)]
    k = 0
    for i in range(n):
        if t[i] != s[i]:
            k += 1
    for i in range(n):
        if t[i] != s[i]:
            if a[ord(t[i]) - 97][ord(s[i]) - 97] != -1:
                # print(k - 2)
                pass
                # print(a[ord(t[i]) - 97][ord(s[i]) - 97] + 1, i + 1)
                pass
                return
            a[ord(s[i]) - 97][ord(t[i]) - 97] = i
    for i in range(n):
        if t[i] != s[i]:
            for j in range(26):
                if a[j][ord(s[i]) - 97] != -1:
                    # print(k - 1)
                    pass
                    # print(a[j][ord(s[i]) - 97] + 1, i + 1)
                    pass
                    return
            a[ord(s[i]) - 97][ord(t[i]) - 97] = i
    # print(k)
    pass
    # print(-1, -1)
    pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(100000)