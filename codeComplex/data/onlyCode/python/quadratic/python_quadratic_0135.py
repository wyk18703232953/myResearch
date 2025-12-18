import sys

# For getting input from input.txt file 
# sys.stdin = open('input.txt', 'r')  
  
# Printing the Output to output.txt file 
# sys.stdout = open('output.txt', 'w') 
# from math import log2
try:    
    # t=int(input())

    # for _ in range(t):
    def check(n):
        count1=0
        s=""
        while(n!=0):
            if n%2:
                count1+=1
                s="1"+s
            else:
                s="0"+s
            n//=2
        return s
    
    def solve(flag,n,l):
        temp_ans=0
        for i in range(n):
            y=(z[flag]^int(l[i],2) )
            b=bin(y)
            temp_ans+=b.count("1")
            flag=not(flag)
        # print(temp_ans)
        return temp_ans
                
    
    
    n=int(input())
    l1 = [input() for y in range(n)]
    temp=input()
    l2 = [input() for y in range(n)]
    temp=input()
    l3 = [input() for y in range(n)]
    temp=input()
    l4 = [input() for y in range(n)]
    
    z=[]
    s=0
    for i in range(n):
       if i%2==1:
           s+=(2**i)
    z.append(s)
    z.append( z[0] ^ (2**n-1) ) 
    ans=m=sys.maxsize
    for i in range(2,17):
        s=check(i)
        if s.count("1")==2:
            s=(4-len(s))*"0"+s
            res=sys.maxsize
            for i in range(4):
                if i==0:
                    x=l1
                elif i==1:
                    x=l2
                elif i==2:
                    x=l3
                else:
                    x=l4
                  
                if s[i]=="1":
                    res+=min(res,solve(1,n,x))
                else:
                    res+=min(res,solve(0,n,x))
            ans=min(ans,res-m)
    print(ans)  

                
except EOFError:
    pass