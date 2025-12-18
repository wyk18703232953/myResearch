tmp = input().split()
n = int(tmp[0])
m = int(tmp[1])

a = list()
b = list()
diff = list()
for i in range(n):
    tmp = input().split()
    a.append(int(tmp[0]))
    b.append(int(tmp[1]))
    diff.append(a[i] - b[i])

diff.sort(reverse=True)

sum_a = sum(a)
i = 0 
while sum_a > m and i < n:
    sum_a = sum_a - diff[i]
    i = i + 1 

if i >= n and sum_a > m:
    print(-1)
else:
    print(i)