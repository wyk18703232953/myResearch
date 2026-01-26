import sys

pl=1

if pl:
	input=sys.stdin.readline
else:	
	sys.stdin=open('input.txt', 'r')
	sys.stdout=open('outpt.txt','w')

def li():
	return [int(xxx) for xxx in input().split()]
def fi():
	return int(input())
def si():
	return list(input().rstrip())	
def mi():
	return 	map(int,input().split())	

		
t=1
while t>0:
	t-=1
	n=fi()
	a=li()
	dp=[[0]*(n+1) for i in range(n+1)]
	for i in range(n-1,-1,-1):
		for j in range(i,n):
			if i==j:
				dp[i][j]=a[i]
			elif i==j-1:
				if a[i]==a[j]:
					dp[i][j]=a[i]+1
			else:
				for k in range(i,j):
					if dp[i][k]	and dp[k+1][j] and dp[i][k]==dp[k+1][j]:
						dp[i][j]=dp[i][k]+1
						break
	ans=[10**18]*(n+1)
	ans[-1]=0

	for i in range(n-1,-1,-1):
		for j in range(i,n):
			if dp[i][j]:
				ans[i]=min(ans[i],1+ans[j+1])
			else:
				ans[i]=min(ans[i],j-i+1+ans[j+1])									
	print(ans[0])
			
