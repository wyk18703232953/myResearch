n, m, k = map(int,input().split())
line = [int(x) for x in input().split()]
line.sort(reverse = True)
count = 0
if k >=m:
    print(count)
    exit(0)
for i in range(n):
    k += line[i]-1
    count += 1
    if k >= m:
        print(count)
        exit(0)
print(-1)