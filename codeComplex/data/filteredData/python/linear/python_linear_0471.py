def main(n):
    # Deterministic data generation
    # c: costs, length n
    c = [(i * 7 + 3) % (n + 5) + 1 for i in range(n)]
    # a: permutation-like mapping with cycles, 0-based indices
    # Map each i to (i+1)%n to ensure a single full cycle; scalable and deterministic
    a = [(i + 1) % n for i in range(n)]

    vis = [-1] * n
    ans = 0
    for i in range(n):
        ind = i
        while vis[ind] == -1:
            vis[ind] = i
            ind = a[ind]
        if vis[ind] == i:
            start = ind
            ind = a[ind]
            cost = c[start]
            while ind != start:
                cost = min(cost, c[ind])
                ind = a[ind]
            ans += cost
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)