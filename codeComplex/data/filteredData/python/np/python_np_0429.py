hell=1000000007
id1=0
id2=0
a = []

def check(n,m,x):
    global id1,id2
    b = [0]*(1<<m)
    idx = [0]*(1<<m)
    for i in range(n):
        mask=0
        for j in range(m):
            if a[i][j]>=x:
                mask=mask^(1<<j)
        b[mask]=1
        idx[mask]=i+1
    for i in range(1<<m):
        if b[i]:
            for j in range(1<<m):
                if b[j]:
                    mask=i|j
                    if mask==((1<<m)-1):
                        id1=idx[i]
                        id2=idx[j]
                        return 1
    return 0

def meowmeow321(n, m):
    global a
    a = []
    for i in range(n):
        row = [((i + 1) * (j + 2)) % hell for j in range(m)]
        a.append(row)
    lo=0
    hi=hell
    while hi-lo>0:
        mid=(hi+lo+1)//2
        if check(n,m,mid):
            lo=mid
        else:
            hi=mid-1
    check(n,m,lo)
    return id1, id2, lo

def main(n):
    if n <= 0:
        return None
    m = max(1, n // 10)
    return meowmeow321(n, m)

if __name__ == "__main__":
    result = main(50)
    print(result)