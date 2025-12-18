N, T = map(int, input().split())

def read_houses():
  for _ in range(N):
    yield tuple(map(int, input().split()))

houses = list(read_houses())

houses.sort()

count = 2 # borders left and right

for (a, x), (b, y) in zip(houses, houses[1:]):
  if b-a - (x/2+y/2) > T:
    count += 2
  if b-a - (x/2+y/2) == T:
    count += 1

print(count)