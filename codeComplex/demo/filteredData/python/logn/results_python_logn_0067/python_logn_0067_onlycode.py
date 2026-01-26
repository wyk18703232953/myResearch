l,r = map(int,input().split())

p = l
lp = -1
while p:
    p = p>>1
    lp+=1

q = r
rp = -1
while q:
    q = q>>1
    rp+=1

s = max(lp,rp)

n=0

while s>=0:
    if l>>s&1!=r>>s&1:
        n |= (r>>s&1)<<s
        break
    s-=1

s-=1

while s>=0:
    n |= 1<<s
    s-=1

print(n)
