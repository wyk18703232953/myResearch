A=[9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889, 8888888889, 98888888889, 1088888888889]
k=int(input())
if k<10:
    print(k)
else:    
    for n in range (0,12):
        if k>A[n+1]:
            continue
        else:
            a=10**(n+1)+(k-A[n]-1)//(n+2)
            b=(k-A[n]-1)%(n+2)
            print(str(a)[b])
            break