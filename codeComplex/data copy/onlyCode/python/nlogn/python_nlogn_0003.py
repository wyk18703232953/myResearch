n, t = [int(item) for item in input().split(' ')]
cont, ans = [], 2
for i in range(n):
    # temp = [float(item) for item in input().split(' ')]
    temp = list(map(int, input().split(' ')))
    house_center, house_len = temp[0], temp[1]
    cont.append([house_center - house_len / 2, house_center + house_len / 2])

# print(cont)

cont.sort(key=lambda element: element[0])
#print(cont)
for i in range(0,n - 1):
    gap = cont[i+1][0] - cont[i][1]
    if gap > t:
        ans += 2
    elif gap == t:
        ans += 1

print(ans)
'''
5 2
10 3
-4 6
50 5
80 4
-30 5
'''
