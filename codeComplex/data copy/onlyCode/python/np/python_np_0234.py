import itertools
n,l,r,x=map(int,input().split())
problems=[int(x) for x in input().split()]
result=0
for i in range(2,n+1):
    for comb in itertools.combinations(problems,i):
        summ = sum(comb)
        mini = min(comb)
        maxx = max(comb)
        if l <= summ <=r and maxx-mini>=x:
            result+=1
print(result)
    		 		 		   	 				 	 		 		 	