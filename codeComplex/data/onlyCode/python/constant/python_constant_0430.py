n,k = map(int,input().split())
if(k - n >= n) :
    print(0)
    exit()
if(k <= n):
    if(k%2):
         print(k//2)
    else :
        print(k//2-1)
else:
    print(n-k//2)