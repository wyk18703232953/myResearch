import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def fun(a,b):
    return (2*(a+b))**2/(a*b)

for i in range (int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    b = []
    i=0
    while(i<n-1):
        if i<n-1 and a[i]==a[i+1]:
            b.append(a[i])
            i+=2
        else:
            i+=1
    m = 10**14
    mi = -1
    for i in range (len(b)-1):
        curr = fun(b[i],b[i+1])
        if curr<m:
            m = curr
            mi = i
    print(b[mi],b[mi],b[mi+1],b[mi+1])