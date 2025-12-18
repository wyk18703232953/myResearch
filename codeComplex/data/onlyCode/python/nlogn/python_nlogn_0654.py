n = int(input())
leafs = set()
other = {}
other_indices = []
s = 0
for i, a in enumerate(map(int, input().split())):
    if a == 1:
        leafs.add(i)
    else:
        other[i] = a
        other_indices.append(i)
    s += a

if not other:
    # n >= 3
    print("NO")
    exit(0)

other_indices.sort(key=lambda index: other[index])
other_indices = [other_indices[-1]] + other_indices[:-1]

edges = []
for i1, i2 in zip(other_indices, other_indices[1:]):
    edges.append((i1, i2))
    other[i1] -= 1
    if other[i1] == 0:
        del other[i1]
    other[i2] -= 1
    if other[i2] == 0:
        del other[i2]

diam = len(other_indices) + min(2, len(leafs))

has_start = has_end = False

while leafs:
    if len(other) == 0:
        print("NO")
        exit(0)
    l = leafs.pop()
    if not has_start and other.get(other_indices[0], 0):
        i = other_indices[0]
        has_start = True
    elif not has_end and other.get(other_indices[-1], 0):
        i = other_indices[-1]
        has_end = True
    else:
        i = next(iter(other))
    edges.append((l, i))
    other[i] -= 1
    if other[i] == 0:
        del other[i]

print("YES", diam - 1)
print(len(edges))
for x, y in edges:
    print(x+1, y+1)
