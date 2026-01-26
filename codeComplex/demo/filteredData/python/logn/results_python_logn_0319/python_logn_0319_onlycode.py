n,k=map(int,input().split())
mod=int(1e9+7)

'''
_2k=2**k

n2k=n*_2k

s=(n2k*(n2k+1))/2
n2k_2k=n2k-_2k

s=s-((n2k_2k)*(n2k_2k+1))/2

s=2*s

s=s/_2k

s=s%mod
print(int(s))
'''

#simplifying above we get:-


if n>0: 
    ans=pow(2,k+1,mod)*n-pow(2,k,mod)+1
else: 
    ans=0
print(ans%mod)