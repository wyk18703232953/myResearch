def check(mid, a, limit):
    res = []
    s = 0
    for r, t, id in a:
        if r >= mid and t + s <= limit:
            res.append(id + 1)
            s += t
        elif t + s > limit:
            break
        if len(res) == mid:
            break
    return res

def f(a, limit):
    a.sort(key=lambda s: s[1])
    ans = None
    lo = 0
    hi = 10**9
    while lo <= hi:
        mid = (lo + hi) // 2
        res = check(mid, a, limit)
        if len(res) >= mid:
            lo = mid + 1
            ans = (res, mid)
        else:
            hi = mid - 1
    print(ans[1])
    print(ans[1])
    print(*ans[0])

def main(n):
    # n: number of items
    # Deterministic generation of (x, y, id)
    # x: requirement, y: time
    limit = n * (n // 2 + 1)

    q = []
    for i in range(n):
        x = (i % (n + 1)) + 1
        y = (i // 2) + 1
        q.append((x, y, i))

    f(q, limit)

if __name__ == "__main__":
    main(10)