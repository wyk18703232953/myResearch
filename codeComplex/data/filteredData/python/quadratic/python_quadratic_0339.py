import string

def main(n):
    if n <= 0:
        return

    lower = string.ascii_lowercase

    # deterministic construction of s1 and s2 of length n
    s1 = [lower[i % 26] for i in range(n)]
    s2 = [lower[(n - 1 - i) % 26] for i in range(n)]

    s1 = list(s1)
    s2 = list(s2)

    count = 0
    ans = []
    np = 0
    for ch in lower:
        if s1.count(ch) != s2.count(ch):
            np += 1
            break
    if np > 0:
        # print(-1)
        pass
        return
    pos = dict()
    for i in range(n):
        if s1[i] in pos:
            pos[s1[i]].append(i)

        else:
            pos[s1[i]] = [i]
    for i in range(n):
        if s1[i] == s2[i]:
            continue

        else:
            row = pos[s2[i]]
            no = 0
            for j in range(len(row)):
                if row[j] > i:
                    no = row[j]
                    break
            for j in range(no, i, -1):
                ans.append(j)
            s1.pop(no)
            s1.insert(i, s2[i])
            pos = dict()
            for j in range(n):
                if s1[j] in pos:
                    pos[s1[j]].append(j)

                else:
                    pos[s1[j]] = [j]
    # print(len(ans))
    pass

    if ans:
        # print(*ans)
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)