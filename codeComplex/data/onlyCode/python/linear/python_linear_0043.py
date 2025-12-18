n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

count = [0]*(int(1e5+1))

for i in arr:
    count[i] += 1

s = sum([1 if i>0 else 0 for i in count])
if s < k:
    print('-1 -1')
    exit()

r = n-1
while True:
    if count[arr[r]] == 1:
        s -= 1
        if s < k:
            s += 1
            break
    count[arr[r]] -= 1
    r -= 1

l=0
while True:
    if count[arr[l]] == 1:
        s -= 1
        if s < k:
            s += 1
            break
    count[arr[l]] -= 1
    l += 1

print(l+1, r+1)

