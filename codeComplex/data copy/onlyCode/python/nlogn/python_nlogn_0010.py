n, t = [int(item) for item in input().split(' ')]
cont, ans = [], 2
for i in range(n):
    hcenter, hlen = [int(item) for item in input().split(' ')]
    cont.append([hcenter - hlen / 2, hcenter + hlen / 2])

# print(f'before => {cont}')
cont.sort(key=lambda item: item[0])
# print(f'after => {cont}')
for i in range(n - 1):
    gap = cont[i + 1][0] - cont[i][1]
    if gap == t:
        ans += 1
    elif gap > t:
        ans += 2

print(ans)