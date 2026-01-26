a=input()
n=len(a)
for i in range(n-1,-1,-1):
    b=sorted([a[j:j+i] for j in range(n-i+1)])
    if True in [b[j]==b[j-1] for j in range(1,n-i+1)]:
        print(i)
        break