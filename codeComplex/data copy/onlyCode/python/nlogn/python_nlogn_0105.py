n = int(input())
arr = list(map(int,input().strip().split()))[:n]


new = sorted(arr)
count = 0

for i in range(n):
    if arr[i] != new[i]:
        count += 1

if count <= 2:
    print('YES')
else:
    print('NO')
