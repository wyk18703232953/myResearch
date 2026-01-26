def solve(x, arr):
    n = len(arr)
    flag = True
    k = []
    i = 0
    while flag:
        sm = 0
        while n > 0 and sm < x:
            sm += int(arr[i])
            i += 1
            n -= 1
            if n <= 0:
                flag = False
                break
        if sm > 0:
            k.append(sm)
    return k

def main(n):
    if n <= 0:
        return
    s = [(i % 2) for i in range(n)]
    s = [str(x) for x in s]
    if len(set(s)) == 1:
        # print('YES')
        pass
        return
    l = []
    t = 0
    for i in range(n - 1):
        t += int(s[i])
        l.append(t)
    v = []
    for i in l:
        if i > 0:
            r = solve(i, s)
            if len(r) > 1 and len(set(r)) == 1:
                # print('YES')
                pass
                break

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)