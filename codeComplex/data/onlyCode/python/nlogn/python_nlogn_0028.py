n = int(input())
l1 = list(input().split())
l2 = []
for i in l1:
    l2.append(int(i))
l1 = set(l2)
l1 = list(l1)
for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] > l1[j]:
            temp = l1[j]
            l1[j] = l1[i]
            l1[i] = temp
if len(l1) > 1:
    print(l1[1])
else:
    print('NO')
