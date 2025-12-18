n,l,r,x = map(int,input().split())
diff = list(map(int,input().split()))

ans = 0
currSum = 0
maxim = 0
minim = 0

for i in range(2**n):

    currSum = 0
    maxim = 0
    minim = 1000001
    ptr = n-1
    
    while i > 0:

        if i & 1:

            currSum += diff[ptr]
            maxim = max(maxim,diff[ptr])
            minim = min(minim,diff[ptr])

        ptr -= 1
        i = i >> 1

    if currSum <= r and currSum >= l:

        if maxim - minim >= x:

            ans += 1

print(ans)
        

        
    
