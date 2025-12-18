from _collections import deque
n = int(input())
m = list(map(int, input().split()))
a = []
b = deque()
 
i = 1
for x in m:
    a.append((x, i))
    i += 1
a.sort(key=lambda p: -p[0])
 
s = input()
ans = []
 
for x in s:
    if x == "1":
        v = b.pop()
        ans.append(v[1])
    else:
        v = a.pop()
        ans.append(v[1])
        b.append(v)
print(*ans)