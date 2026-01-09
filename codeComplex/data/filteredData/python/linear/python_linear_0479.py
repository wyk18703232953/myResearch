def main(n):
    # Deterministic construction of c and a based on n
    # c[1..n], a[1..n], with 1-based indexing and dummy 0 at index 0
    c = [0] + [(i * 3 + 7) % (n + 5) + 1 for i in range(1, n + 1)]
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        # Create a deterministic functional graph with cycles
        # Map each i to ((i * 2 + 3) % n) + 1 to ensure in [1, n]
        a[i] = ((i * 2 + 3) % n) + 1

    vis = [0] * (n + 1)
    ans = 0
    for i in range(1, n + 1):
        x = i
        while vis[x] == 0:
            vis[x] = i
            x = a[x]
        if vis[x] != i:
            continue
        v = x
        mn = c[x]
        while a[x] != v:
            x = a[x]
            mn = min(mn, c[x])
        ans += mn
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)