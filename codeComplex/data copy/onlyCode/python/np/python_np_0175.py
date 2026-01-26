from itertools import combinations
n, l, r, x = map(int,input().split())
a = list(map(int,input().split()))
print(sum([sum([max(j) - min(j) >= x and l <= sum(j) <= r for j in combinations(a, i)]) for i in range(2, n + 1)]))




# Made By Mostafa_Khaled