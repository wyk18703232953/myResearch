def main(n):
    if n <= 0:
        print(0)
        return
    c = [0] + [i % 10 + 1 for i in range(1, n + 1)]
    a = [0] + [((i + 1) if i < n else 1) for i in range(1, n + 1)]
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
    print(ans)


if __name__ == "__main__":
    main(10)