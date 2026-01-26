
import itertools

n , l , r , x = map(int,input().split())

problems = list(map(int,input().split()))

ans = 0

for i in range(2 , n + 1 ):
    for j in itertools.combinations(problems ,i):
        if (l <= sum(j) <= r and max(j) - min(j) >= x):
            ans +=1

print(ans)


