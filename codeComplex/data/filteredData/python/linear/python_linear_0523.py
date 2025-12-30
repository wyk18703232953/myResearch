import random

def main(n: int):
    # 1. 生成一棵 n 个节点的随机树（节点编号 1..n）
    # 使用简单的随机生成：对于每个节点 i (2..n)，随机连到 [1, i-1] 之一
    edges = []
    for i in range(2, n):
        parent = random.randint(1, i - 1)
        edges.append((parent, i))
    if n > 1:
        parent = random.randint(1, n - 1)
        edges.append((parent, n))

    # 2. 用生成的边构造 dict1（邻接表）
    dict1 = {}
    for x, y in edges:
        if y not in dict1:
            dict1[y] = []
        dict1[y].append(x)

        if x not in dict1:
            dict1[x] = []
        dict1[x].append(y)

    # 3. 生成测试访问序列 arr（长度为 n）
    #   为了让逻辑能有 Yes/No 两种情况，可以随机生成一个包含 1..n 的排列
    arr = list(range(1, n + 1))
    random.shuffle(arr)

    # 4. 按原逻辑处理（移除 input，使用生成的数据）
    if arr[0] != 1:
        print("No")
        return

    j = 0
    i = 1
    flag = 0  # 原代码中未使用 flag，这里保持一致
    while i < n and j < n:
        # 若 dict1 中没有 arr[i] 这个键，则其邻接表视为空列表
        neighbors = dict1.get(arr[i], [])
        if arr[j] in neighbors:
            i += 1
        else:
            j += 1

    if i != n and j == n:
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    # 举例：调用 main(5)
    main(5)