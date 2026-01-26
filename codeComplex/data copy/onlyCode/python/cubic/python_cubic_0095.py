n,k= map(int,input().split(' '))
l= list(map(int,input().split(' ')))
f =list(map(int,input().split(' ')))
h=list(map(int,input().split(' ')))
d1=dict({(a,0) for a in f})
d2=dict({(a,0) for a in f})
for a in l:
	if(a in d1):d1[a]+=1
for a in f:
	d2[a]+=1
#print(d1,d2)
dp = [[0 for i in range(520*12)] for j in range(520)]
#print(len(dp), len(dp[0]))
for x in range(n+1):
	for y in range(n*k+1):
		for i in range(k+1):
				dp[x+1][y+i] = max(dp[x+1][y+i],+dp[x][y]+(0 if i==0 else h[i-1]) )
ss=0
for i in d1:
	#print(dp[d1[i]][d2[i]])
	ss+=dp[d2[i]][d1[i]]
print(ss)