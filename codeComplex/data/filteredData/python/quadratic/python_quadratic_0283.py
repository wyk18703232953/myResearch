n,m=map(int,(10,5))
seq=[i%7 for i in range(1,n+1)]
f=[(i*2)%7 for i in range(1,m+1)]
a=[]
for i in range(n):
    for j in range(m):
        if seq[i]==f[j]:
            a.append(seq[i])
for i in range(len(a)):
    print(a[i],end=' ')

def main(n):
    m = max(1, n//2)
    seq=[(i*3)%10 for i in range(1,n+1)]
    f=[(i*5)%10 for i in range(1,m+1)]
    a=[]
    for i in range(n):
        for j in range(m):
            if seq[i]==f[j]:
                a.append(seq[i])
    for i in range(len(a)):
        print(a[i],end=' ')
    print()

if __name__ == "__main__":
    main(10)