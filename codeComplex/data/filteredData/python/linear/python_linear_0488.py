def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main(n):
    # n is the number of intervals
    # Deterministically generate n intervals [l, r] with l <= r
    # Example pattern: l = i, r = i + (i % 5) + 1 ensures r >= l+1
    from collections import defaultdict

    d = defaultdict(int)
    ll = defaultdict(list)
    rr = defaultdict(list)
    llst = []
    rlst = []
    lst = []

    for i in range(n):
        l = i
        r = i + (i % 5) + 1
        if l > r:
            l, r = r, l
        lst.append([l, r])
        llst.append(l)
        rlst.append(r)
        ll[l].append(r)
        rr[r].append(l)

    if n == 0:
        # print(0)
        pass
        return

    left = max(llst)
    right = min(rlst)
    lleft = min(ll[left])
    lright = max(rr[right])

    # First removal: remove [left, lleft]
    lst.remove([left, lleft])
    if lst:
        pl = max(i[0] for i in lst)
        pr = min(i[1] for i in lst)
        mx = max(0, pr - pl)

    else:
        mx = 0
    lst.append([left, lleft])

    # Second removal: remove [lright, right]
    lst.remove([lright, right])
    if lst:
        pl = max(i[0] for i in lst)
        pr = min(i[1] for i in lst)
        mx = max(mx, max(0, pr - pl))

    # print(mx)
    pass
if __name__ == "__main__":
    main(10)