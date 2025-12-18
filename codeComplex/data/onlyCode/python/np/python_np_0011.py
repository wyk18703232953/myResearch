import sys
input=sys.stdin.readline

def count_bits(x):
    cnt=0
    for i in range(n):
        if((1<<i)&x):
            cnt+=1
    return(cnt)

n=int(input())
a=[list(map(float,input().split())) for i in range(n)]
dp=[0 for i in range(1<<n)] #Probabilty a particular permutation of (alive) fish are acheived.
dp[-1]=1 #We start with all fish, so the probability they all together is 1(base case)
#We will calculate the probability of acheiving a particular permutation of k alive fish from all possible permutations of k+1 alive fish for all values of k.
for mask in range((1<<n)-1,-1,-1):
    val=count_bits(mask)
    total=val*(val-1)//2 #Used to calculate the probability of choosing two fish among the alive fish. We will take the case the first fish eats the second fish(the opposite case is dealt again in another loop, won't increase efficiency much), and add to the new permutation the probability of obtaiining it from the current permutation.
    for i in range(n):
        if(mask&(1<<i)==0): #We can't choose a dead/eaten fish
            continue
        for j in range(n): #Second fish of the pair for the above choosen fish among all other alive fish
            if(mask&(1<<j)==0 or i==j):
                continue
            dp[mask^(1<<j)]+=dp[mask]*a[i][j]/total #considering ith fish eats jth fish
for i in range(n):
    print(dp[1<<i])
