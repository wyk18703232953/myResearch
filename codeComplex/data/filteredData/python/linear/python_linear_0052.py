import random

def find(u, par):
    if u != par[u]:
        par[u] = find(par[u], par)
    return par[u]

def union(u, v, par):
    u = find(u, par)
    v = find(v, par)
    par[u] = v

def main(n):
    # 1. 生成测试数据
    # 随机生成数组 p，元素范围适当放大，避免过多重复
    p = [random.randint(1, 2 * n) for _ in range(n)]
    # 随机生成 a, b
    a = random.randint(1, 3 * n)
    b = random.randint(1, 3 * n)

    # 2. 原逻辑
    mp = dict()
    for i in range(n):
        mp[p[i]] = i + 1

    par = [i for i in range(n + 2)]

    for i in range(n):
        union(i + 1, mp.get(a - p[i], n + 1), par)
        union(i + 1, mp.get(b - p[i], 0), par)

    A = find(0, par)
    B = find(n + 1, par)

    if A != B:
        print('YES')
        print(' '.join(['1' if find(i, par) == B else '0' for i in range(1, n + 1)]))
    else:
        print('NO')

# 示例调用
if __name__ == "__main__":
    main(10)