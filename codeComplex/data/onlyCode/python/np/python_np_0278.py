def pow2(n):
    j=0
    while(n%2==0):
        n//=2
        j+=1
    return j    
n,q=map(int,input().split())
for j in range(q):
    u=int(input())
    s=input()
    for k in range(len(s)):
        num=pow2(u)
        if(s[k]=="R" and num!=0):
            u=u+2**(num-1)
        elif(s[k]=="L" and num!=0):
            u=u-2**(num-1)
        elif(s[k]=="U" and u!=(n+1)//2):
            m1=u+2**(num)
            m2=u-2**(num)
            if(pow2(m1)==(num+1)):
                u=m1
            else:
                u=m2
    print(u)                