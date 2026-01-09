def main(n):
    # Generate deterministic test data based on n
    # s and t are strings of length n over lowercase letters
    # Use simple periodic patterns to ensure mismatches exist for analysis.
    l = [chr(i + 97) for i in range(26)]
    s = [l[i % 26] for i in range(n)]
    t = [l[(i + 1) % 26] for i in range(n)]

    d = {}
    ans = 0
    x, y = -1, -1

    for i in range(n):
        if s[i] != t[i]:
            d[(s[i], t[i])] = i
            ans += 1

    for i in l:
        for j in l:
            if (i, j) in d and (j, i) in d:
                ans -= 2
                x = d[(i, j)] + 1
                y = d[(j, i)] + 1
                break
        if x != -1:
            break

    if x == -1 and y == -1:
        for i in l:
            for j in l:
                for k in l:
                    if (i, j) in d and (j, k) in d:
                        ans -= 1
                        x = d[(i, j)] + 1
                        y = d[(j, k)] + 1
                        break
                if x != -1:
                    break
            if x != -1:
                break

    # print(ans)
    pass
    # print(x, y)
    pass
if __name__ == "__main__":
    main(10)