import sys
import math

prime=[True for _ in range(1000001)]

# # Remove these 2 lines while submitting your code online
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
def solve():
    n,e,h,a,b,c=map(int,input().split())
    ans=1e9
    for i in range(1,1000001):
        su=0
        ntmp=n
        tmp1=e
        tmp2=h
        tmp1-=i
        tmp2-=i
        if (tmp1<0 or tmp2<0 or i>ntmp):
            break
        ntmp-=i
        su+=(c*i)
        if (ntmp==0):
            ans=min(ans,su)
            continue
        if (a<=b):
            if ((tmp1//2)>=ntmp):
                su+=int(a*ntmp)
                ntmp-=ntmp
            else:
                su+=int(a*(tmp1//2))
                ntmp-=(tmp1//2)
                if (ntmp<=(tmp2//3)):
                    su+=int(b*ntmp)
                    ntmp-=ntmp
                else:
                    su+=int(b*(tmp2//3))
                    ntmp-=(tmp2//3)
        else:
            if ((tmp2//3)>=ntmp):
                su+=int(b*ntmp)
                ntmp-=ntmp
            else:
                su+=int(b*(tmp2//3))
                ntmp-=(tmp2//3)
                if (ntmp<=(tmp1//2)):
                    su+=int(a*ntmp)
                    ntmp-=ntmp
                else:
                    su+=int(a*(tmp1//2))
                    ntmp-=(tmp1//2)
        if (ntmp==0):
            ans=min(ans,su)
    # print(ans)
    if (ans==1e9):
        print("-1")
    else:
        print(ans)

def main():
    n=int(input())
    s=input()
    m={}
    have={}
    cc=0
    for c in s:
        if (c not in m):
            m[c]=1
        else:
            m[c]+=1
    ct=len(m)
    l=0
    ans=1e9
    for i in range(0,n):
        if (s[i] not in have):
            have[s[i]]=0
            cc+=1
        have[s[i]]+=1
        while(l<=i and have[s[l]]>1):
            have[s[l]]-=1
            l+=1
        if (cc==ct):
            ans=min(ans,i-l+1)
    print(ans)

if __name__ == "__main__":
    main()