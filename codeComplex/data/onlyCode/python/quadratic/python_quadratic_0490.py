def main():
    def update(l, r, i, res):
        j = 0
        while j < i:
            if res[j] is None:
                r[j] -= 1
                if r[j] < 0:
                    return False
            j += 1
        j += 1
        while j < n:
            if res[j] is None:
                l[j] -= 1
                if l[j] < 0:
                    return False
            j += 1
        return True

    ilist = {1}
    n = int(input())
    res = [None] * n
    cur = n
    l = [int(x) for x in input().split()]
    r = [int(x) for x in input().split()]

    while ilist and (sum(l) != 0 or sum(r) != 0):
        ilist = set()
        for i in range(n):
            if l[i] == r[i] == 0 and res[i] is None:
                res[i] = cur
                ilist.add(i)
        for i in ilist:
            check = update(l, r, i, res)
            if not check:
                return False
        cur -= 1
    if not ilist:
        return False
    for i in range(n):
        if res[i] is None:
            res[i] = cur
    return res


if __name__ == '__main__':
    res = main()
    if not res:
        print('NO')
    else:
        print('YES')
        for x in res:
            print(x, end=' ')