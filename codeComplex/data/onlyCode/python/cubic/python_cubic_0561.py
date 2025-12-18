a = input()
b = input()
la = [int(x) for x in a]
res = []
la.sort()
la = la[::-1]
lb = [int(x) for x in b]
cnt = [0] * 20

def check():
    tres = 0
    for x in range(len(res)):
        tres *= 10
        tres += int(res[x])
    return tres <= int(b)
if len(a) < len(b):
    for i in range(len(la)):
        print(la[i], end = '')
    print()
else:
    for i in range(len(la)):
        cnt[la[i]] += 1
    flag = 0
    for i in range(len(lb)):
        if flag == 0 and cnt[lb[i]]:
            res.append(lb[i])
            cnt[lb[i]] -= 1
        else:
            flag = i - 1
            for j in range(lb[i] - 1, -1, -1):
                if cnt[j]:
                    res.append(j)
                    cnt[j] -= 1
                    break
            for j in range(9, -1, -1):
                while cnt[j]:
                    res.append(j)
                    cnt[j] -= 1
            break
    while not check():
        temp = []
        cnt = [0] * 20
        for x in range(flag):
            temp.append(res[x])
            cnt[res[x]] -= 1
        for i in la:
            cnt[i] += 1
        ##print("cnt = ", cnt)
        res = temp
        ##print(flag, res)
        for v in range(lb[flag] - 1, -1, -1):
            if cnt[v]:
                res.append(v)
                cnt[v] -= 1
                break
        for v in range(9, -1, -1):
            while cnt[v]:
                res.append(v)
                cnt[v] -= 1
        ##print(flag, res)
        flag -= 1
    for i in range(len(res)):
        print(res[i], end = '')
    print()
