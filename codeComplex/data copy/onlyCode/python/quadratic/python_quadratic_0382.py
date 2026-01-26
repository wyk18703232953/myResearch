n, m = map(int,input().split())
r=0
c=0
f= 1
for i in range(n):
    s = input()
    if  f and "B" in s:
        f = 0
        ci = s.index('B')
        cc = s.count("B")
        r = i+1+cc//2
        c = ci+cc//2+1
print(r,c)