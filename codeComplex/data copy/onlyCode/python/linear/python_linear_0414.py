n,k = map(int, input().split())
s = input()
l = []
for i in s:
    a = ord(i)-96
    if a not in l:
        l.append(a)
l.sort()
c = l[0]
a = 1
b = l[0]
for i in range(1,len(l)):
    if a==k:
        break
    if (l[i]-b)>1:
        a += 1
        c += l[i]
        b = l[i]
if a<k:
    print(-1)
else:
    print(c)