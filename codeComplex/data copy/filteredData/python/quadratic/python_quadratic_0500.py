import sys
import threading

ans = []

def dfs(g, i, p):
    global ans
    count = 0
    for j in g[i]:
        if j == p:
            continue
        count += dfs(g, j, i)
    if count == 0:
        count = 1
    ans.append(count)
    return count

def solve_generated(n):
    global ans
    ans = []

    if n <= 0:
        # print()
        pass
        return

    # 构造一个确定性的树：父节点为 i//2（i>=2）
    g = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        p = i // 2
        g[i].append(p)
        g[p].append(i)

    dfs(g, 1, 0)
    ans.sort()
    st = ' '.join(map(str, ans))
    # print(st)
    pass

def main(n):
    solve_generated(n)

if __name__ == "__main__":
    # 示例：用 n=10 运行一次
    main(10)