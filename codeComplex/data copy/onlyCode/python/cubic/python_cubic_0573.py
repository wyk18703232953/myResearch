def get_smallest(m, l):
    res = ''
    for i in "0123456789":
        if m.get(i, 0):
            if i == l:
                res += i * (m[i] - 1)
            else:
                res += i * m[i]
    return res 

a = input()
b = input()

if len(a) < len(b):
    a = sorted(a)
    a.reverse()
    print(''.join(a))
elif a == b:
    print(a)
else:
    cmap = dict()
    for i in a:
        cmap[i] = cmap.get(i, 0) + 1

    cur = 0
    res = ''
    gm = False 

    while cur < len(a):
        for i in "9876543210":
            if cmap.get(i, 0):
                if cur == len(a) - 1 or i < b[cur] or gm:
                    res += i
                    cmap[i] -= 1
                    gm = True
                    break
                elif i == b[cur]:
                    if get_smallest(cmap, i) <= b[cur + 1:]:
                        res += i
                        cmap[i] -= 1
                        break
        cur += 1

    print(res)