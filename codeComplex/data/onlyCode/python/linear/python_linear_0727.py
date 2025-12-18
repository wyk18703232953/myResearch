N, K = map(int, input().split())
if N == K:
    print("0"*N)
elif K == 1:
    print("0"*(N-1) + "1")
elif K == 3:
    print("1" + "0"*(N-4) + "101")
else:
    res = ["0"]*N
    for i in range(0, N, N//2-K//2+1):
        res[i] = "1"
    print(''.join(res))