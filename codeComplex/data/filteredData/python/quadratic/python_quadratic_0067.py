import random

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

def main(n):
    # 生成测试数据：一个长度为 n 的随机排列，元素范围 [0, n-1]
    lista = list(range(n))
    random.shuffle(lista)

    # 生成查询次数 m 和区间 [l, r]
    # 这里 m 取 n，查询为随机合法区间
    m = n
    queries = []
    for _ in range(m):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 逻辑与原代码相同
    invercount = 0
    bitTree = [0] * (n + 2)

    # 由于原代码把元素值当作 BIT 的索引使用，
    # 要确保索引不越界，因此这里 BIT 的大小取 n+2，
    # 且元素值范围为 [0, n-1] 是安全的。
    for k in reversed(lista):
        updatebit(bitTree, n + 1, k, 1)
        counter = getsum(bitTree, k - 1)
        invercount += counter

    for l, r in queries:
        summa = ((r - l + 1) * (r - l)) / 2
        if (invercount + summa) % 2:
            print('odd')
            invercount = 1
        else:
            print('even')
            invercount = 0