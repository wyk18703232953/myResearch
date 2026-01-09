def main(n):
    # Interpret n as number of nodes in a tree
    if n < 2:
        # Degenerate small case: no edges, emulate minimal behavior
        a = 1
        s = {1: []}

    else:
        a = n
        s = {i: [] for i in range(1, a + 1)}
        # Deterministically generate a tree with n nodes.
        # For simplicity, create a "star-like" structure but gradually:
        # Connect node i to i//2 for i >= 2, ensuring a tree.
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
        # print("No")
        pass
    elif c == 0:
        # print("Yes")
        pass
        # print(1)
        pass
        for i in range(1, a + 1):
            if len(s[i]) == 1:
                # print(i, end=" ")
                pass
        # print()
        pass

    else:
        # print("Yes")
        pass
        # print(len(s[ans]))
        pass
        k = []
        for i in range(1, a + 1):
            if len(s[i]) == 1:
                k.append(i)
        for i in k:
            # print(min(ans, i), max(ans, i))
            pass
if __name__ == "__main__":
    main(10)