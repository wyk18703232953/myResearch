def main(n):
    # Generate deterministic test data based on n
    # s and d are both lists of characters of length n
    # First half of positions: s[i] = 'a', second half: 'b'
    # d is a right rotation of s by 1, so they are always anagrams
    s = ['a' if i < n // 2 else 'b' for i in range(n)]
    d = s[-1:] + s[:-1] if n > 0 else []

    # Core logic from original program
    if sorted(s) != sorted(d):
        # print(-1)
        pass
        return

    else:
        ans = []
        for i in range(n):
            if s[i] != d[i]:
                ind = -1
                for u in range(i + 1, n):
                    if s[u] == d[i]:
                        ind = u
                        break

                    else:
                        ind = -1
                if ind == -1:
                    # print(-1)
                    pass
                    return
                cnt = abs(ind - i)
                s.pop(ind)
                s.insert(i, d[i])
                for k in range(cnt):
                    if ind > 0:
                        ans.append(ind)

                    else:
                        ans.append(1)
                    ind -= 1
        # print(len(ans))
        pass

        if ans:
            # print(*ans)
            pass
if __name__ == "__main__":
    main(10)