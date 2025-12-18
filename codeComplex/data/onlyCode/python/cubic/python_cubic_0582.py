import sys
import math
#input=sys.stdin.readline
#t=int(input())
t=1
for _ in range(t):
    #n=int(input())
    #c,m,x=map(int,input().split())
    #l=list(map(int,input().split()))
    a=input()
    b=input()
    dp=[0]*(11)
    for i in a:
        dp[int(i)]+=1
    #print(dp)
    if len(b)>len(a):
        ans=''
        for i in range(len(a)):
            for j in range(9,-1,-1):
                if dp[j]!=0:
                    ans+=str(j)
                    dp[j]-=1
                    break
    elif len(a)==len(b):
        ans=''
        a1=[]
        cmpr=''
        i=0
        while i<len(a):
            cmpr+=b[i]
            #print(cmpr,ans,dp)
            if i==0:
                flag=0
                for j in range(9,0,-1):
                    if ans+str(j)<=cmpr and dp[j]!=0:
                        flag=1
                        dp[j]-=1
                        ans+=str(j)
                        a1.append(j)
                        break
                if flag==0:
                    dp[1]-=1
                    a1.append(1)
                    ans+='1'
            else:
                flag=0
                for j in range(9,-1,-1):
                    if ans+str(j)<=cmpr and dp[j]!=0:
                        flag=1
                        ans+=str(j)
                        a1.append(j)
                        dp[j]-=1
                        break
                
                if flag==0:
                    ch=0
                    for i1 in range(i-1,-1,-1):
                        if ch==1:
                            break
                        for j1 in range(int(ans[i1])-1,-1,-1):
                            if i1==0:
                                if j1>0 and dp[j1]!=0:
                                    dp[a1[i1]]+=1
                                    dp[j1]-=1
                                    index=i1
                                    a1.pop()
                                    a1.append(j1)
                                    ch=1
                                    break
                            else:
                                if  dp[j1]!=0:
                                    dp[a1[i1]]+=1
                                    dp[j1]-=1
                                    a1.pop()
                                    index=i1
                                     
                                    a1.append(j1)
                                    ch=1
                                    break
                            if ch==1:
                                break
                        if ch==1:
                            break
                        val=a1.pop()
                        dp[val]+=1
                            #print(13,dp,a1)
                            
                    ans=''
                    cmpr=''
                    #print(13,dp,a1)
                    dp=[0]*11
                    for i1 in range(len(a)):
                        dp[int(a[i1])]+=1
                    #print('check  ',dp,a1)
                    for i1 in range(len(a1)):
                        dp[a1[i1]]-=1
                        
                    for i1 in range(len(a1)):
                        ans+=str(a1[i1])
                        cmpr+=b[i1]
                    i=index    
                    #print(11,ans,cmpr,a1,dp)
            i+=1                
    print(ans)    