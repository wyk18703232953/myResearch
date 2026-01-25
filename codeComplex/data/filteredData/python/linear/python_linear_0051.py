parent = [i for i in range(100002)]

def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp

def generate_input(n):
    # 保证有足够的 parent 空间
    global parent
    size_needed = max(100002, n + 5)
    if len(parent) < size_needed:
        parent = [i for i in range(size_needed)]
    else:
        for i in range(size_needed):
            parent[i] = i

    # 确定性生成 n, a, b, lst
    # n 为规模参数本身
    if n <= 0:
        n_val = 1
    else:
        n_val = n

    # 让 a, b 与 lst 有一定结构但保持确定性
    # 例如：a = 2*n_val + 3, b = 3*n_val + 5
    a = 2 * n_val + 3
    b = 3 * n_val + 5
    # lst 为长度为 n_val 的整数序列
    # 使用简单的算术构造，避免重复太简单：lst[i] = (i*2 + 1) % (4*n_val + 7)
    mod = 4 * n_val + 7
    lst = [(i * 2 + 1) % mod for i in range(n_val)]
    return n_val, a, b, lst

def core_logic(n, a, b, lst):
    temp = {lst[i]: i for i in range(n)}
    for i in range(n):
        if a - lst[i] in temp:
            unionSet(i, temp[a - lst[i]])
        else:
            unionSet(i, n)
        if b - lst[i] in temp:
            unionSet(i, temp[b - lst[i]])
        else:
            unionSet(i, n + 1)

    pa = findSet(n)
    pb = findSet(n + 1)
    if pa == pb:
        return "NO", []
    else:
        res = [0 if findSet(i) == pb else 1 for i in range(n)]
        return "YES", res

def main(n):
    n_val, a, b, lst = generate_input(n)
    result, assignment = core_logic(n_val, a, b, lst)
    print(result)
    if result == "YES":
        print(*assignment)

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)