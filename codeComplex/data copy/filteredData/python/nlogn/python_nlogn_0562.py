def main(n):
    if n < 2:
        # print("Yes")
        pass
        return

    # Deterministically build a tree: star centered at 1
    # Edges: (1,2),(1,3),...,(1,n)
    visited = [False for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    l = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        a, b = 1, i
        l[a].append(b)
        l[b].append(a)

    # Deterministically build permutation b of [1..n]
    # Ensure 1 is first, then 2..n
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
                # print("No")
                pass
                t = False
                break

        else:
            c += aux
            c1 += 1
            continue
        break
    if t:
        # print("Yes")
        pass
if __name__ == "__main__":
    main(10)