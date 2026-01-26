
from itertools import permutations, chain

def get_plots(a,b):

  ax,ay = a
  bx,by = b

  for x in range(ax,bx,1 if ax < bx else -1):
    yield (x,ay)
  for y in range(ay,by,1 if ay < by else -1):
    yield (bx,y)

def solve(points):

  for a,b,c in permutations(points):
    ax,ay = a
    bx,by = b
    cx,cy = c
    if min(ax,bx) <= cx <= max(ax,bx) and min(ay,by) <= cy <= max(ay,by):
      return list(chain(get_plots(a,c), get_plots(c,b), [b]))

  def it():
    for a,b,c in permutations(points):
      ax,ay = a
      bx,by = b
      m = (ax,by)
      L = list(chain(get_plots(a,m),get_plots(b,m), get_plots(c,m), [m]))
      yield (len(L),L)

  return min(it())[1]



points = [tuple(map(int,input().split())) for _ in range(3)]

res = solve(points)
print(len(res))
for x,y in res:
  print(x,y)
