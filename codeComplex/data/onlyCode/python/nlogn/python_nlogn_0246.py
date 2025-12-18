def next(A,n, x):
    l = 0
    r = n-1
    p = -1
    while l <= r:
        m = (l+r)//2


        if A[m] <= x:
            l = m+1
        else:
            p = m
            r = m-1
    return p


N, Q = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

P = []
P.append(A[0])

for i in range(1, N):
    P.append(P[i-1] + A[i])

soldiers = P[-1]
arrows = 0


for q in range(Q):

    arrows += B[q]
    if arrows >= soldiers:
        arrows = 0
        print(N)
    else:
        ind = next(P, N, arrows)
        print(N- ind)



