from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())

graph = [[] for _ in range(n)]
leaf = -1
for _ in range(n-1):
    a,b = map(int,stdin.readline().split())
 
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

def bfs(G, s):
    # la cola comienza con el vertice desde el cual hacemos bfs
    Q = deque() 
    Q.append(s) 
    
    # al inicio todas las distancias comienzan en infinito, por las 
    # restricciones del problema ningun camino va a ser de ese tamanno
    infinite = 10 ** 6
    d = [infinite]*n 

    parent = [-1]*n
    valid = True

    # la distancia del vertice raiz es 0
    d[s] = 0 

    while Q:
        # visitamos u
        u = Q.popleft() 
        
        not_visited_count = 0

        # visitamos cada adyacente de u
        for v in G[u]: 
            # si no lo hemos visitado, le ponemos distancia y 
            # lo agregamos a la cola para visitar sus adyacentes
            if d[v] == infinite:
                d[v] = d[u] + 1
                parent[v] = u
                Q.append(v)
                not_visited_count += 1
        
        if not_visited_count < 3 and d[u] != k:
            valid = False

    # retornamos el array d, que es el de las distancias del 
    # nodo s al resto de los nodos del grafo            
    return d, parent, valid

leaf = -1
for i,v in enumerate(graph):
    if len(v) == 1:
        leaf = i
        break

d, parent, _ = bfs(graph,leaf)
center = -1
farthest_leaf = -1
diameter = 2*k

for i,level in enumerate(d):
    if level == diameter:
        farthest_leaf = i
        break
    
if len(graph[farthest_leaf]) != 1 or farthest_leaf == -1:
    print("NO")
    exit()


for _ in range(k):
    center = parent[farthest_leaf]
    farthest_leaf = center

if center == -1:
    print("NO")
    exit()

_, _, valid = bfs(graph,center)

if valid:
    print("YES")
else:
    print("NO")

 




