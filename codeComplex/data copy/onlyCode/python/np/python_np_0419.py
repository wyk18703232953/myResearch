# import builtins

debug = 0
BIG = 10 ** 9 + 1

input = raw_input


def prof(f):
    return f
    # if 'profile' in dir(builtins):
    #     return profile(f)
    # else:
    #     return f


def report(f):
    def new_f(x):
        res = f(x)
        # print(f"{x}  --> {res}")
        return res

    return new_f if debug else f


def mcheck(a, pairs):
    m = len(a[0])
    allm = 2 ** m - 1

    subs = {i: {i} for i in range(allm + 1)}

    for i in range(allm + 1):
        for j in range(i):
            if i | j == i:  # 11 1  10 1   00 0  01 1
                subs[i].add(j)

    mx = [max(aa) for aa in a]

    @prof
    def check(v):
        masks = {0: -1}
        done = [False] * (allm + 1)
        for i, aa in enumerate(a):
            if mx[i] < v:
                continue
            c = sum(1 << b for b in range(len(aa)) if aa[b] >= v)
            # if c == allm:
            #     pairs[v] = i, i
            #     return True
            if not done[c]:
                for cc in subs[c]:
                    if allm - cc in masks:
                        other = masks[allm - c]
                        pairs[v] = i, other
                        return True
                    masks[cc] = i
                    done[cc] = True
                # masks[c] = i
        # for ma, mb in itertools.combinations(masks, 2):
        #     if ma | mb == allm:
        #         pairs[v] = masks[ma], masks[mb]
        #         return True
        return False

    return check


@prof
def go():
    n, m = map(int, input().split())

    a = []
    # mx = 0
    # mnmx = 0
    uniq = set()
    for _ in range(n):
        aa = tuple(map(int, input().split()))
        # mx = max(mx, max(aa))
        # mnmx = max(mnmx, min(aa))
        a.append(aa)
        uniq.update(aa)

    uniq = sorted(uniq)
    pairs = {0: (0, 0)}
    check = mcheck(a, pairs)
    l = 0
    r = len(uniq) - 1
    while l != r:
        if debug: print(l, r)
        if l + 1 == r:
            if check(uniq[r]):
                l = r
            else:
                r = l
            continue
        c = (l + r) // 2
        if check(uniq[c]):
            l = c
        else:
            r = c

    l = uniq[l]
    if debug: print(l, pairs[l])
    if l not in pairs:
        check(l)
    a = pairs[l][0]
    b = pairs[l][1]
    if b == -1:
        b = a

    print("%d %d" % (a + 1, b + 1))


go()
