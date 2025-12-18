from sys import *
mod=1000000007
n,q=map(int,stdin.readline().split())
s=str(stdin.readline())
arr=[]
count=0
for i in s:
	if(i=='1'):
		count+=1
	arr.append(count)
#q=int(input())
ansarr=[]
for i in range(q):
	x,y=map(int,input().split())
	if(x==1):
		total1=arr[y-1]
	else:
		total1=arr[y-1]-arr[x-2]
	total0=(y-x+1-total1)	
	ans=pow(2,y-x+1,mod)%mod
	ans=((((ans%mod)-(pow(2,total0,mod)%mod))%mod)+mod)%mod	
	ansarr.append(ans)
stdout.write('\n'.join(map(str, ansarr)))