def main(n):
    # Generate deterministic strings s and t of length n over a small alphabet
    # so that the algorithm has non-trivial work but remains reproducible.
    if n <= 0:
        # print(-1)
        pass
        return

    alphabet = ['a', 'b', 'c']
    s = [alphabet[i % len(alphabet)] for i in range(n)]
    t = [alphabet[(i * 2 + 1) % len(alphabet)] for i in range(n)]

    if sorted(t) == sorted(s):
        ans = []
        for i in range(n - 1, -1, -1):
            if t[i] != s[i]:
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