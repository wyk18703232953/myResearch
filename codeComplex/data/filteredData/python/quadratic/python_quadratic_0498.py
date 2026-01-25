import sys
from collections import defaultdict

def main(n):
    # 构造确定性的父节点数组 par（长度 n-1，表示一棵树）
    # 使用简单算术规则：第 i+2 个节点的父亲是 (i % (i+1)) + 1，保证在 1..i+1 范围内
    if n <= 0:
        return
    par = [(i % (i + 1)) + 1 for i in range(1, n)]

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
    sys.stdout.write(' '.join(map(str, bulb)))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 规模
    main(10)