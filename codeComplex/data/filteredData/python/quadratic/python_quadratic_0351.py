def main(n):
    # Deterministically generate s and t of length n
    # s: cyclic lowercase letters from 'a'
    # t: s rotated right by 1 position (guaranteed transformable by adjacent swaps)
    s = [chr(ord('a') + (i % 26)) for i in range(n)]
    t = s[-1:] + s[:-1] if n > 0 else []

    ans = []
    # Core algorithm unchanged
    for i in range(n):
        for j in range(i, n):
            if s[j] == t[i]:
                for k in range(j, i, -1):
                    s[k], s[k - 1] = s[k - 1], s[k]
                    ans.append(k)
                break

    if s == t:
        # print(len(ans))
        pass

        if ans:
            # print(' '.join(map(str, ans)))
            pass

        else:
            # print()
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)