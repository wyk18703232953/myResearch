from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())

graph = [set() for _ in range(n)]

for _ in range(n-1):
    a,b = map(int,stdin.readline().split())

    graph[a - 1].add(b - 1)
    graph[b - 1].add(a - 1)

leafs = [i for i,v in enumerate(graph) if len(v) == 1]
new_leafs = []
valid = True
centers = dict()
count = 0

while len(leafs) > 1 and valid:
    for leaf in leafs:
        center = graph[leaf].pop()

        try:
            centers[center] += 1
        except KeyError:
            centers[center] = 1

        graph[center].remove(leaf)

        if len(graph[center]) == 0:
            break

        elif len(graph[center]) == 1:
            new_leafs.append(center)

    if any(mult < 3 for mult in centers.values()):
        valid = False
        break
    
    count = count + 1
    leafs = new_leafs
    new_leafs = []
    centers = {}

if valid and count == k:
    print("YES")
else:
    print("NO")
