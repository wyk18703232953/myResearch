def main(n):
    # Map n to original problem's n and k
    # Here: original n = n, k = max allowed group size = n (or any deterministic function of n, e.g. n//2+1)
    orig_n = n
    k = n // 2 + 1 if n > 0 else 1

    # Generate deterministic P: sequence of integers in [0, 255]
    # Use a simple modular pattern to keep values within 0..255 as in original code
    P = [(i * 37 + 13) % 256 for i in range(orig_n)]

    parent = list(range(256))
    sz = [1] * 256

    def rt(x):
        if x != parent[x]:
            parent[x] = rt(parent[x])
        return parent[x]

    def u(rx, ry):
        parent[ry] = rx
        sz[rx] += sz[ry]

    ans = [0] * orig_n
    for i, p in enumerate(P):
        rx = rt(p)
        while rx > 0 and sz[rx] + sz[rt(rx - 1)] <= k:
            u(rt(rx - 1), rx)
            rx = rt(p)
        ans[i] = rt(p)

    # For timing experiments you might want to avoid large prints;
    # here we keep the original behavior.
    # print(' '.join(map(str, ans)))
    pass
if __name__ == "__main__":
    main(10)