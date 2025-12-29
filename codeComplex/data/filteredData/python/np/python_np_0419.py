import random

debug = 0
BIG = 10 ** 9 + 1


def prof(f):
    return f


def report(f):
    def new_f(x):
        res = f(x)
        return res

    return new_f if debug else f


def mcheck(a, pairs):
    m = len(a[0])
    allm = 2 ** m - 1

    subs = {i: {i} for i in range(allm + 1)}

    for i in range(allm + 1):
        for j in range(i):
            if i | j == i:
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
            if not done[c]:
                for cc in subs[c]:
                    if allm - cc in masks:
                        other = masks[allm - c]
                        pairs[v] = (i, other)
                        return True
                    masks[cc] = i
                    done[cc] = True
        return False

    return check


@prof
def go(a):
    uniq = set()
    for aa in a:
        uniq.update(aa)

    uniq = sorted(uniq)
    pairs = {0: (0, 0)}
    check = mcheck(a, pairs)
    l = 0
    r = len(uniq) - 1
    while l != r:
        if debug:
            print(l, r)
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
    if debug:
        print(l, pairs[l])
    if l not in pairs:
        check(l)
    a_idx = pairs[l][0]
    b_idx = pairs[l][1]
    if b_idx == -1:
        b_idx = a_idx

    print("%d %d" % (a_idx + 1, b_idx + 1))


def main(n):
    # 生成测试数据：
    # n 行，每行 m 个整数。此题逻辑依赖列数 m，设为一个小常数。
    m = 3
    # 数值范围
    low, high = 1, 10 ** 9

    random.seed(0)
    a = [
        tuple(random.randint(low, high) for _ in range(m))
        for _ in range(n)
    ]

    go(a)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)