from sys import stdin
input=stdin.readline

def count(n):

    value=0
    while(n):
        n &= (n-1)
        value+=1

    return value

def nc2(n):
    return (n*(n - 1))//2

def answer():

    dp=[0]*(1 << n) #fishes

    #let 1 be alive fishes
    #let 0 be dead fishes

    dp[(1 << n) - 1]=1 #initially let all be alive


    for mask in range((1 << n) - 1,0,-1):

        m=count(mask) # count alive fishes
        if(m==1):continue

        #probability of selecting 2 alive fishes
        p=1/(nc2(m))
       
        #pairing 2 fishes
        for i in range(n):
            for j in range(n):
                if(i==j):continue
                #check if i , j fishes are alive or not

                if((mask >> i & 1) and (mask >> j & 1)):
                    #let fish i eat j
                    next_mask=mask ^ (1 << j)
                    dp[next_mask]+=(dp[mask]*p*a[i][j])

    for i in range(n):
        #fish i is alive
        print(dp[1 << i],end=' ')
    
n=int(input())
a=[list(map(float,input().split())) for i in range(n)]

answer()
print()
