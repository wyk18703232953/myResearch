def main(n):
    # Interpret n as the length of the string s
    # Deterministically construct a lowercase string of length n
    # Pattern: cyclic through 'a' to 'z'
    s = ''.join(chr(97 + (i % 26)) for i in range(n))

    # Define k as a deterministic function of n, but bounded and >= 1
    # For example, k = min(10, max(1, n // 3))
    k = min(10, max(1, n // 3))

    # Core logic from original program
    l = []
    for ch in s:
        val = ord(ch) - 96
        if val not in l:
            l.append(val)
    l.sort()

    if not l:
        # print(-1)
        pass
        return

    c = l[0]
    a = 1
    b = l[0]
    for i in range(1, len(l)):
        if a == k:
            break
        if (l[i] - b) > 1:
            a += 1
            c += l[i]
            b = l[i]
    if a < k:
        # print(-1)
        pass

    else:
        # print(c)
        pass
if __name__ == "__main__":
    main(100)