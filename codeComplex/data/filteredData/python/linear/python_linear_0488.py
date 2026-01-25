from collections import defaultdict


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main(n):
    d = defaultdict(int)
    ll = defaultdict(list)
    rr = defaultdict(list)
    llst = []
    rlst = []
    lst = []

    for i in range(n):
        l = i
        r = i + (n // 2)
        lst.append([l, r])
        llst.append(l)
        rlst.append(r)
        ll[l].append(r)
        rr[r].append(l)

    left = max(llst)
    right = min(rlst)
    lleft = min(ll[left])
    lright = max(rr[right])

    lst.remove([left, lleft])
    pl = max(i[0] for i in lst)
    pr = min(i[1] for i in lst)
    mx = max(0, pr - pl)

    lst.append([left, lleft])
    lst.remove([lright, right])
    pl = max(i[0] for i in lst)
    pr = min(i[1] for i in lst)
    result = max(mx, max(0, pr - pl))

    print(result)
    return result


if __name__ == "__main__":
    main(10)