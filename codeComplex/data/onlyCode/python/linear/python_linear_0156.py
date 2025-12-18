arr = []
d = {}
for _ in range(int(input())):
    s = input()
    a,b,c = tuple(map(int, s.replace("(","").replace(")","").replace("/",".").replace("+",".").split(".")))
    x = (a+b)/c
    arr.append(x)
    if x not in d:
        d[x] = 0
    d[x] += 1

for i in arr:
    print(d[i], end = " ")