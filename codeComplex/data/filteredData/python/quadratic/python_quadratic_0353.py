def main(n):
    # Deterministically generate s and t of length n
    # s: repeating pattern of lowercase letters
    letters = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = letters[:]  # base sequence
    # t: rotate s by (n // 3) positions to keep it an anagram
    shift = n // 3 if n > 0 else 0
    t = s[shift:] + s[:shift]

    s = list(s)
    t = list(t)

    if sorted(t) == sorted(s):
        ans = []
        for i in range(n - 1, -1, -1):
            if t[i] != s[i]:
                # find first occurrence of t[i] at or before i
                j = s.index(t[i])
                for k in range(j, i):
                    s[k], s[k + 1] = s[k + 1], s[k]
                    ans.append(str(k + 1))
        # print(len(ans))
        pass

        if ans:
            # print(' '.join(ans))
            pass

        else:
            # print()
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)