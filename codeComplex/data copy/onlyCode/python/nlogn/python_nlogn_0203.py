from sys import stdin
input=stdin.readline
def check(mid,a,limit):
	res=[]
	s=0
	for r,t,id in a:
		if r>=mid and t+s<=limit:
			res.append(id+1)
			s+=t
		elif t+s>limit:
			break
		if len(res)==mid:
			break
	# print(res,s)
	return res

def f(a,limit):
	a.sort(key=lambda s:s[1])
	ans=None
	lo=0
	hi=len(a)+1
	while lo<=hi:
		mid=(lo+hi)//2
		res=check(mid,a,limit)
		if len(res)>=mid:
			lo=mid+1
			ans=(res,mid)
		else:
			hi=mid-1
	print(ans[1])
	print(ans[1])
	print(*ans[0])


n,limit=map(int,input().strip().split())
q=[]
for i in range(n):
	x,y=map(int,input().strip().split())
	q.append((x,y,i))
f(q,limit)