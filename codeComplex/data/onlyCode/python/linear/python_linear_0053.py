def findSet(u):
  if parents[u] != u:
    parents[u] = findSet(parents[u])
  return parents[u]


def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return
  
  if ranks[up] > ranks[vp]:
    parents[vp] = up
  elif ranks[up] < ranks[vp]:
    parents[up] = vp
  else:
    parents[up] = vp
    ranks[vp] += 1
    
n, a, b = map(int, input().split())
ps = list(map(int, input().split())) 

mapping = set(ps)

parents = {x: x for x in ps}
parents['A'] = 'A'
parents['B'] = 'B'
ranks = {x: 0 for x in ps}
ranks['A'] = 0
ranks['B'] = 0
# print(parents)
result = True
for x in ps:
  if a - x in mapping:
    unionSet(x, a - x)
  else:
    unionSet(x, 'B')
    
  if b - x in mapping:
    unionSet(x, b - x)
  else:
    unionSet(x, 'A')
  # print(parents)

# print(parents)
if findSet('A') == findSet('B'):
  print("NO")
  
else:
  print("YES")
  for i in ps:
    if findSet(i) == findSet('A'):
      print("0", end = ' ')
    else:
      print("1", end = ' ')
