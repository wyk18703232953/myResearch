p = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
d = 0
for x in arr:
    d += x
c = 0
num = 0
while c <= d/2:
    c += arr[num]
    num += 1
print(num)
