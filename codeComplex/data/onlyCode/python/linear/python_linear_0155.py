n, p = map(int, input().split())
list1 = list(map(int, input().split()))
mx = 0
curr = 0
nxt = sum(list1)
for i in range(n - 1):
    curr += list1[i]
    nxt -= list1[i]
    mx = max(mx, curr % p + nxt % p)
print(mx)