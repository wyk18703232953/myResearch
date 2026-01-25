import sys
from collections import defaultdict

def build_input(n):
    # n as number of nodes
    if n <= 1:
        n = 2
    # construct a simple deterministic parent array for a rooted tree
    # parent of node i (2..n) is i//2
    par = [i // 2 for i in range(2, n + 1)]
    return n, par

def algorithm(n, par):
    graph = defaultdict(list)
    bulb = [1] * (n + 1)
    for i in range(n - 1):
        bulb[par[i]] = 0
        graph[par[i]].append(i + 2)
    for i in range(n, 0, -1):
        if bulb[i] == 0:
            count = 0
            for j in graph[i]:
                count += bulb[j]
            bulb[i] = count
    bulb = bulb[1:]
    bulb.sort()
    return bulb

def main(n):
    n_input, par = build_input(n)
    result = algorithm(n_input, par)
    sys.stdout.write(' '.join(map(str, result)))

if __name__ == "__main__":
    main(10)