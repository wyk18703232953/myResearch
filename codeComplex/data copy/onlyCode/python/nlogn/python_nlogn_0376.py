n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a = sorted(a)

cur_v = a[0]
cur_count = 1
ans = 0

# print(a)
for i in range(1, len(a)):

    if a[i] > a[i-1] and a[i] > a[i-1]+k:
        ans += cur_count
        cur_count = 1
    elif a[i] == a[i-1]:
        cur_count += 1
    elif a[i] > a[i-1]:
        cur_count = 1
        
ans += cur_count

        
print(ans)