import sys

def getsum(BITTree, i):
    i = i + 1
    s = 0
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s

def updatebit(BITTree, n, i, v):
    i = i + 1
    while i <= n:
        BITTree[i] += v
        i += i & (-i)

def build_input(n):
    if n < 1:
        n = 1
    # 原程序输入结构：
    # n
    # lista: n 个整数，数值范围在 [1, n]
    # m
    # m 行查询，每行为 l r
    #
    # 这里将 n 作为数组长度，m 也设为 n
    # lista 设为 1..n 的逆序，这样可控且确定性
    size = n
    lista = [size - i for i in range(size)]
    m = n
    queries = []
    for i in range(m):
        l = (i % size) + 1
        r = size
        if l > r:
            l, r = r, l
        queries.append((l, r))
    return size, lista, m, queries

def core_logic(size, lista, m, queries):
    invercount = 0
    bitTree = [0] * (size + 2)
    for k in reversed(lista):
        updatebit(bitTree, size + 1, k, 1)
        counter = getsum(bitTree, k - 1)
        invercount += counter
    outputs = []
    for (l, r) in queries:
        summa = ((r - l + 1) * (r - l)) / 2
        if (invercount + summa) % 2:
            outputs.append('odd')
            invercount = 1
        else:
            outputs.append('even')
            invercount = 0
    return outputs

def main(n):
    size, lista, m, queries = build_input(n)
    results = core_logic(size, lista, m, queries)
    for line in results:
        print(line)

if __name__ == "__main__":
    main(10)