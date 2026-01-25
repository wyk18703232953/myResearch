def main(n):
    # Generate deterministic test data based on n
    # s: first n lowercase letters cyclically starting from 'a'
    # t: reversed s
    s = [chr(ord('a') + (i % 26)) for i in range(n)]
    t = s[::-1]

    ans = []
    # Core algorithm logic preserved
    for i in range(n):
        for j in range(i, n):
            if s[j] == t[i]:
                for k in range(j, i, -1):
                    s[k], s[k - 1] = s[k - 1], s[k]
                    ans.append(k)
                break
    if s == t:
        print(len(ans))
        if ans:
            print(' '.join(map(str, ans)))
        else:
            print()
    else:
        print(-1)


if __name__ == "__main__":
    # Example deterministic call
    main(5)