def main(n):
    if n < 2:
        print("Yes")
        return

    # Deterministically generate a tree: a simple chain 1-2-3-...-n
    visited = [False for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    l = [[] for _ in range(n + 1)]
    for i in range(1, n):
        a = i
        b_edge = i + 1
        l[a].append(b_edge)
        l[b_edge].append(a)

    # Deterministically generate b as [1, 2, 3, ..., n]
    b = [i for i in range(1, n + 1)]

    s = [1]
    visited[1] = True
    c = 1
    c1 = 0
    t = True
    while len(s) != n:
        aux = 0
        for i in l[s[c1]]:
            if not visited[i]:
                visited[i] = True
                dp[i] = 1
                aux += 1
        for i in range(c, c + aux):
            if dp[b[i]] == 1:
                s.append(b[i])
                dp[b[i]] = 0
            else:
                print("No")
                t = False
                break
        else:
            c += aux
            c1 += 1
            continue
        break
    if t:
        print("Yes")


if __name__ == "__main__":
    main(10)