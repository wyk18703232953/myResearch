from itertools import combinations

p, minn, maxn, dif = map(int, input().split())
(*lst,) = map(int, input().split())
print(sum([sum([(maxn>=sum(j)>=minn)and((max(j)-min(j))>=dif) for j in combinations(lst,i)]) for i in range(2,p+1)]))
