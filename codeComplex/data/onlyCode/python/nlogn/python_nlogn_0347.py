n = int(input())
a = [int(i) for i in input().split()]

d = {}
power = [2**i for i in range(31)]
ans = []
for i in a:
    d[i] = 0

for num in d.keys():
    for p in power:
        if num+p in d:
            ans = [num, num+p]
            if num+p+p in d:
                print(3)
                ans.append(num+p+p)
                print(*ans)
                exit()
if ans:
    print(2)
    print(*ans)
else:
    print(1)
    print(a[0])
