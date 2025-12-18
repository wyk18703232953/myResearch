n, t = [int(item) for item in input().split(' ')]
cont, ans = [], 2
for i in range(n):
    hcenter, hlen = [float(item) for item in input().split(' ')]
    # subArr = [hcenter - hlen / 2, hcenter + hlen / 2]
    # cont.append(subArr)
    cont.append([hcenter - hlen / 2, hcenter + hlen / 2])

# print(f'cont before => {cont}')
cont.sort(key=lambda it: it[0])
# print(f'cont  after => {cont}')
for i in range(n - 1):
    gap = cont[i + 1][0] - cont[i][1]
    if gap > t:
        ans += 2
    elif gap == t:
        ans += 1
print(ans)