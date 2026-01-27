k1,k2,k3=map(int,input().split())
a=[k1,k2,k3];a=sorted(a)
#
dp=[0]*5001;dp[0]=1
i=0
while i<=5000:
 if dp[i]==0 and i+a[0]<=5000:
   while i+a[0]<=5000:
     dp[i]=1
     i=i+a[0]
 else:i+=1
#print(dp)
#
i=0
while i<=5000:
 if dp[i]==0 and i+a[1]<=5000:
   while i+a[1]<=5000:
     dp[i]=1
     i=i+a[1]
 else:i+=1
#print(dp)
#
i=0
while i<=5000:
 if dp[i]==0 and i+a[2]<=5000:
   while i+a[2]<=5000:
     dp[i]=1
     i=i+a[2]
 else:i+=1
#
dp=dp[:2002]
if dp.count(0)==0:print("YES")
else:print("NO")
