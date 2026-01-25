def main(n):
    # Interpret n as number of nodes in a tree
    if n < 2:
        a = 2
    else:
        a = n

    # Deterministically generate a tree on a nodes.
    # Use a simple pattern: connect i to i//2 for i from 2 to a.
    s = {}
    for i in range(1, a + 1):
        s[i] = []
    for i in range(2, a + 1):
        v = i // 2
        c = i
        s[v].append(c)
        s[c].append(v)

    ans = 0
    c = 0
    for i in range(1, a + 1):
        if len(s[i]) > 2:
            c += 1
            ans = i
    if c > 1:
        print("No")
    elif c == 0:
        print("Yes")
        print(1)
        for i in s:
            if len(s[i]) == 1:
                print(i, end=" ")
    else:
        print("Yes")
        print(len(s[ans]))
        k = []
        for i in s:
            if len(s[i]) == 1:
                k.append(i)
        for i in k:
            print(min(ans, i), max(ans, i))


if __name__ == "__main__":
    main(10)