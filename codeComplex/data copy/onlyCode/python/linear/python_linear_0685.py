n = int(input())
b = list(map(int, input().split()))
ff = []
ss = []
for i in  b[::-1]:
    q = i
    f = q // 2
    if q % 2:
        s = f + 1
    else:
        s = f
    if len(ff) == 0:
        ff = [f]
        ss = [s]
    else:
        if f > ff[-1] or s < ss[-1]:
            d = max(f - ff[-1], ss[-1] - s)
            f -= d
            s += d
        ff.append(f)
        ss.append(s)
print(*(ff[::-1] + ss))