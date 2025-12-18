n = int(input())
l = list(map(int, input().split()))
ansl = ['sjfnb', 'cslnb']
ans = -1
d = dict()
val = 0
if n == 1:
    ans = (l[0] + 1) % 2
else:
    l.sort()
    for elem in l:
        d[elem] = d.get(elem, 0) + 1
    hm = 0
    which = -1
    i = 0
    for elem in d.values():
        if elem >= 2:
            hm += 1
            which = i
        i += 1
    which = list(d.keys())[which]
    if max(d.values()) >= 3 or d.get(0, 0) >= 2 or hm > 1:
        ans = 1
    elif hm == 1 and d.get(which - 1, 0) > 0:
        ans = 1
    else:
        for i in range(n):
            val += l[i] - i
        ans = (val + 1) % 2
print(ansl[ans])