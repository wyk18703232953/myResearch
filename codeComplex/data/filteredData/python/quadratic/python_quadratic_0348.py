def main(n):
    # Deterministic data generation
    # s and t are permutations of the same multiset so that sorted(s) == sorted(t)
    # s: 'a', 'b', 'c', ... cycling over 26 letters
    # t: reverse of s to make it non-trivial but always transformable
    if n <= 0:
        return

    base_chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = base_chars[:]          # list of characters
    t = base_chars[::-1]       # reversed list as target string
    t = ''.join(t)             # original code uses string for t

    i, r = 0, []

    if sorted(s) != sorted(t):
        # print(-1)
        pass

    else:
        while i < n:
            j = i
            while j < n and s[j] != t[i]:
                j += 1
            s[i:j + 1] = s[j:j + 1] + s[i:j]
            r.extend(range(j, i, -1))
            i += 1
        # print(len(r))
        pass

        if r:
            # print(*r)
            pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)