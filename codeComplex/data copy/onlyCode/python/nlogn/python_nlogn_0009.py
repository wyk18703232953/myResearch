n, t = [int(item) for item in input().split(' ')]
cont, ans = list(), 2
for i in range(n):
    hCenter, hLen = [float(item) for item in input().split(' ')]
    # subArr = [hCenter - hLen / 2, hCenter + hLen / 2]
    # cont.append(subArr)
    cont.append([hCenter - hLen / 2, hCenter + hLen / 2])

#print(f'before=> {cont}')
cont.sort(key=lambda item: item[0])
#print(f'after=> {cont}')
for i in range(n - 1):
    gap = cont[i+1][0] - cont[i][1]
    if gap > t:
        ans += 2
    elif gap == t:
        ans += 1

print(ans)
