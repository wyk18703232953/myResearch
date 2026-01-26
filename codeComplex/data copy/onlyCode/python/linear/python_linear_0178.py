def ints():
 return list(map(int,input().split()))
n,k=ints()
a,t=ints(),ints()
ans=sum(a[ii] for ii in range(n) if t[ii])
bb=[a[ii] if t[ii]==0 else 0 for ii in range(n)]
ll=0
rr=k
tmp=sws=sum(bb[:k])
while rr<n:
 sws-=bb[ll]
 sws+=bb[rr]
 ll+=1
 rr+=1
 tmp=max(tmp,sws)
ans+=tmp
print(ans)
 			 	  		 		 	   	 	 	  	 			