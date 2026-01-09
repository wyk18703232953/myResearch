def main(n):
    # Generate deterministic data based on n
    a = [(i * 2 + 1) % 100000 for i in range(n)]
    s = 0
    for i in range(n):
        for j in range(i):
            s ^= a[j] > a[i]
    # Let q scale with n deterministically
    q = n
    for i in range(q):
        l = i % n
        r = (i * 2 + 3) % n
        if l > r:
            l, r = r, l
        s ^= (r - l + 1) * (r - l) // 2 % 2
        # print(['even', 'odd'][s])
        pass
if __name__ == "__main__":
    main(10)