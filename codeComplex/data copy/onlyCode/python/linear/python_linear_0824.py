
n,k = map(int,input().split())

for puts in range(10**9):
    candy = puts*(puts+1)//2
    if candy - (n-puts) == k:
        print(n-puts)
        exit(0)





