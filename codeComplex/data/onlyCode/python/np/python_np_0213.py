from itertools import combinations

p, minn, maxn, dif = map(int, input().split())
(*lst,) = map(int, input().split())
c = 0
for i in range(2, p + 2):
    for j in combinations(lst, i):
        if (maxn >= sum(j) >= minn) and (max(j) - min(j) >= dif):
            c += 1
print(c)