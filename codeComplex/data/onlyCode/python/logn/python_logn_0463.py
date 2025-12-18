print("? 0 0")
t = int(input())
A=[]
B=[]
a=0
b=0
for i in range(30):
    A.append(-1)
    B.append(-1)
i = 29
d = 2**i
while i>=0:
    a+=d
    b+=d
    print("?", end=' ')
    print(a, end=' ')
    print(b)
    s=int(input())
    if s == -t:
        if s==1:
            A[i]=0
            B[i]=1
            b-=d
            print("?", end=' ')
            print(a, end=' ')
            print(b)
            t=int(input())
        elif s==-1:
            A[i]=1
            a-=d
            B[i]=0
            print("?", end=' ')
            print(a, end=' ')
            print(b)
            t=int(input())
    i-=1
    d//=2
d=1
for j in range(30):
    if A[j]==-1:
        a = a^d
        print("?", end=' ')
        print(a, end=' ')
        print(b)
        s = int(input())
        if s==1:
            A[j]=1
            B[j]=1
        else:
            A[j]=0
            B[j]=0
        a = a^d
    d*=2
d=1
a=0
b=0
for i in range(30):
    a+=d*A[i]
    b+=d*B[i]
    d*=2
print("!", end=' ')
print(a, end=' ')
print(b)
