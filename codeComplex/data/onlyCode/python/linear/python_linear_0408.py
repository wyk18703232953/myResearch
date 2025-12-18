n,k =  map(int,input().split())

def tonny(i) :
	return (ord(i)-96)
a= sorted(input())
a=list(map(tonny,a))
a=sorted(list(set(a)))
ans=[a.pop(0)]
k-=1
for j in a :
	if j-ans[-1] >1 and k>0 :
		k-=1
		ans.append(j)
	if k==0 :
		break
if k!=0 :
	print(-1)
else:
	print(sum(ans))
