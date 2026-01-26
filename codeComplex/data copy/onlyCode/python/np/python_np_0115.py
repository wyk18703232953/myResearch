m = int(input())
values = []
idx = []
for i in range(m):
    x = int(input())
    ans = 0
    for xx,ii in zip(values,idx):
        if (xx^x) < x:
            x^=xx
            ans^=ii
    if x == 0:
        anss = []
        for j in range(i):
            if (ans&1)==1:
                anss.append(j)
            ans>>=1
        print(len(anss),*anss)
    else:
        print(0)
        values.append(x)
        idx.append(ans^(2**i))
