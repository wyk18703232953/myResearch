n = int(input())

if n == 3:
    print('1 1 3')
    exit()
if n == 1:
    print('1')
    exit()
if n == 2:
    print('1 2')
    exit()
d = 2
ans = []
lfn = n
while d <= n:
    k = n // d
    for j in range(lfn - k):
        ans.append(d//2)
    lfn = n - len(ans)
    d *=2
d //= 2
k = n/d
if k < 1.5:
    ans.append(d)
else:
    ans.append(d + d//2)
print(' '.join([str(i) for i in ans]))