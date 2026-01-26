def digisum(n):
    count = 0
    while(n>0):
        count+=n%10
        n = n//10
    return count

n,s = list(map(int,input().split()))
l,r = 1,n
flag = 0
while l<r:
    m = l+(r-l)//2
    digi_sum = digisum(m)
    num = m
    if num-digi_sum>=s:
        flag = 1
        cur = m
        r = m
    else:
        l = m+1
    if r-l==1:
        digi_sum = digisum(l)
        num = l
        if num-digi_sum>=s:
            flag = 1
            cur = l
            break
        digi_sum = digisum(r)
        num = r
        if num-digi_sum>=s:
            flag = 1
            cur = r
            break
if flag==0:
    digi_sum = digisum(l)
    num = l
    if num-digi_sum>=s:
        flag = 1
        cur = l
if flag==0:
    print(0)
else:
    print(n-cur+1)