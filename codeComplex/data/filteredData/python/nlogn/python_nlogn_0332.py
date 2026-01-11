def main(n):
    # Deterministically generate n strings
    # Example pattern: "a", "ab", "abc", ..., increasing prefixes of alphabet repeated
    base = "abcdefghijklmnopqrstuvwxyz"
    l = []
    for i in range(1, n + 1):
        s = "".join(base[j % len(base)] for j in range(i))
        l.append([len(s), s])

    # Original logic
    l.sort()
    ch = 1
    nn = n
    ans = []
    for i in range(nn - 1):
        if l[i][1] not in l[i + 1][1]:
            ch = 0
            break

        else:
            ans.append(l[i][1])

    if ch and nn > 0:
        ans.append(l[nn - 1][1])
        # print("YES")
        pass
        # print(*[x for x in ans], sep="\n")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(5)