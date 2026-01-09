import sys
import threading

def dfs(g, i, p, ans):
    count = 0
    for j in g[i]:
        if j == p:
            continue
        count += dfs(g, j, i, ans)
    if count == 0:
        count = 1
    ans.append(count)
    return count

def solve(n):
    l = [i for i in range(1, n)] if n > 1 else []
    g = [[] for _ in range(n + 1)]
    for i in range(1, n):
        g[i + 1].append(l[i - 1])
        g[l[i - 1]].append(i + 1)
    ans = []
    dfs(g, 1, 0, ans)
    ans.sort()
    st = ' '.join(map(str, ans))
    # print(st)
    pass

def main(n):
    max_recur_size = 10**5 * 2 + 1000
    max_stack_size = max_recur_size * 500
    sys.setrecursionlimit(max_recur_size)
    threading.stack_size(max_stack_size)
    thread = threading.Thread(target=solve, args=(n,))
    thread.start()
    thread.join()

if __name__ == "__main__":
    main(10)