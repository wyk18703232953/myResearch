import sys
input = sys.stdin.readline

test=int(input())
for tests in range(test):
    S=input().strip()
    t=input().strip()

    LENS=len(S)
    LENT=len(t)
    flag=0

    for i in range(1,LENT+1):
        t1=t[:i]
        t2=t[i:]

        DP=[-1]*(len(t1)+1)
        DP[0]=0

        for s in S:
            for j in range(len(t1),-1,-1):
                if 0<=DP[j]<len(t2) and s==t2[DP[j]]:
                    DP[j]+=1
                    
                if s==t1[j-1]:
                    DP[j]=max(DP[j],DP[j-1])

                #print(s,j,DP)

        if DP[-1]==len(t2):
            print("YES")
            flag=1
            break
    else:
        print("NO")

    #print(S,t,t1,t2,DP)
                    
                    
        

        
        
        
