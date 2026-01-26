# map(int, input().split(" "))
n = int(input())
l = list(map(int, input().split(" ")))
l2 = list(map(int, input().split(" ")))
dp_1 = l2.copy()
dp_2 = [9999999999]*n
dp_3 = [9999999999]*n
for i in range(1, n):
    for j in range(i):
        if l[i] > l[j]:
            dp_2[i] = min(dp_2[i], dp_1[j]+l2[i])

for i in range(1,n):
    for j in range(i):
        if l[i] > l[j]:
            dp_3[i] = min(dp_3[i], dp_2[j]+l2[i])

x = min(dp_3)
if x == 9999999999:
    print(-1)
else:
    print(x)