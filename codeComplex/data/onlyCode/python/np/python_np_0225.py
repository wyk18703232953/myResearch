from itertools import combinations
n , l , r ,x = map(int,input().split())
a = list(map(int, input().split()))
c = 0
for i in range(1,n+1):
    for j in combinations(a,i):
        if (l<=sum(j)<=r and max(j)-min(j)>=x):
            c+=1
print(c)