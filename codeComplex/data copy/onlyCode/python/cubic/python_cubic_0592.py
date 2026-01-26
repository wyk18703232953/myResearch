def get(g):
    s = [str(i) for i in g]
    num = int("".join(s))
    return num

a = input()
b = input()
bb = int(b)
mark = [0 for i in range(len(a))]
c = a
f = []
g = []

for i in range(0 , len(a)):
    g.append(a[i])

g.sort()
g.reverse()
num = get(g)

index = []
if num <= bb:
    print(num)
    exit(0)


for i in range(0 , min(len(a) , len(b))):
    mx = '-1'
    idx = 0
    for j in range(0 , len(a)):
        if mark[j] == 0 and a[j] <= b[i]:
            if a[j] > mx:
                mx = a[j]
                idx = j



    if mx == '-1':
        rem = []

        while True and len(f) > 0:
            ma = '-1'
            id = 0
            for j in range(0 , len(a)):
                if mark[j] == 0 and a[j] < f[-1]:
                    if a[j] > ma:
                        ma = a[j]
                        id = j

            if ma == '-1':
                mark[index.pop()] = 0
                f.pop()
                continue
            else:
                mark[index.pop()] = 0
                f.pop()
                f.append(ma)
                mark[id] = 1
                break


        for j in range(0, len(a)):
            if mark[j] == 0:
                rem.append(a[j])

        rem.sort()
        rem.reverse()

        for j in rem:
            f.append(j)

        print(get(f))
        exit(0)

    elif mx < b[i] and mx != '-1':
        f.append(mx)
        mark[idx] = 1
        index.append(idx)
        break
    elif mx == b[i] and mx != '-1':
        f.append(mx)
        mark[idx] = 1
        index.append(idx)

rem = []

for i in range(0 , len(a)):
    if mark[i] == 0:
        rem.append(a[i])

rem.sort()
rem.reverse()

for i in rem:
    f.append(i)

print(get(f))



