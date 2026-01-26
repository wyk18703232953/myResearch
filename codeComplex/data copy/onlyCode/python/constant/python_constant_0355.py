kol = int(input())

dic = {'purple': 'Power',
       'green': 'Time',
       'blue': 'Space',
       'orange': 'Soul',
       'red': 'Reality',
       'yellow': 'Mind'}

r = []
g = []
missing = 6 - kol

for k in range(kol):
    rocks = input()
    r.append(rocks)

for key in dic:
    if r.count(key) == 0:
        g.append(dic[key])

print(missing)

for stone in g:
    print(stone)