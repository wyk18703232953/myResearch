mod = 10**9+7
x,k = [int(x) for x in input().split()]
if x ==0:
    print(0)
else:
    T = [1]
    for j in range(1024):
        T.append((2*T[-1])%(mod))
    L = [1]
    for i in range(10**6):
        L.append(((T[1024])*L[-1])%(mod))
        
    k =k % (mod-1)
    
    t1 = (k)%(1024)
    t2 =(k+1)%(1024)
    
    q1 = k//(1024)
    q2 =(k+1)//(1024)
    
    A = (L[q2]*T[t2])%(mod)
    A *= x
    A = A % (mod)
    
    B = (L[q1]*T[t1])%(mod)
    
    print((A-B+1)%(mod))
