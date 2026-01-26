n,s = map(int,input().split())
if s>=n:
    print('0')
else:
    for i in range(s,n+2):
        l=0
        for j in str(i):
            l+=int(j)
        if i-l>=s:
            break
    print(n-i+1)