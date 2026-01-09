import sys

def main(n):
    # 约定：给定 n，构造一个确定性的 (N, D, K)
    # 为了让原算法在不同规模下都能运行，这里让 N 随 n 线性增长
    # 并用简单算术从 n 推导 D 和 K
    N = max(2, n)              # 原程序中的 n：节点数
    D = max(1, min(N - 1, n // 3 + 1))  # 原程序中的 d：主链长度
    K = max(1, min(5, n // 5 + 1))      # 原程序中的 k：度上限

    # 原始逻辑开始（用 N, D, K 替代输入）
    n_val = N
    d = D
    k = K

    if n_val <= d:
        # print('NO')
        pass
        return
    if k == 1 and n_val > 2:
        # print('NO')
        pass
        return

    edgestot = []
    edges = [[] for _ in range(n_val)]
    tovisit = []
    for i in range(d):
        edgestot.append([i, i + 1])
        tovisit.append([i + 1, min(i + 1, d - i - 1)])
        edges[i].append(i + 1)
        edges[i + 1].append(i)
    cur = d + 1
    while cur < n_val and len(tovisit) > 0:
        x = tovisit.pop()
        if x[1] == 0:
            continue
        while len(edges[x[0]]) < k and cur < n_val:
            tovisit.append([cur, x[1] - 1])
            edgestot.append([cur, x[0]])
            edges[x[0]].append(cur)
            edges[cur].append(x[0])
            cur += 1

    if len(edgestot) == n_val - 1:
        # print('YES')
        pass
        for i in range(n_val - 1):
            # print(edgestot[i][0] + 1, edgestot[i][1] + 1)
            pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    # 示例：固定调用若干不同规模，确保行为可复现
    for test_n in [3, 5, 10]:
        main(test_n)