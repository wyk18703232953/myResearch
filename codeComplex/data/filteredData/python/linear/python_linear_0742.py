import random

def main(n, qnum=None, arr=None, queries=None, seed=0):
    """
    n: 规模（数组长度）
    qnum: 查询个数；若为 None，则设为 n
    arr: 初始数组；若为 None，则自动随机生成长度为 n 的数组
    queries: 查询列表；若为 None，则自动随机生成 qnum 个查询
    seed: 随机种子，方便复现
    """
    random.seed(seed)

    # 生成测试数据
    if qnum is None:
        qnum = n

    if arr is None:
        # 生成 1..10^9 范围内的随机整数
        arr = [random.randint(1, 10**9) for _ in range(n)]
    else:
        # 确保长度为 n
        assert len(arr) == n, "arr length must be n"

    if queries is None:
        # q 的有效范围为 1..(任意大)，但算法是周期性的；
        # 为了测试，生成 1..(2*n) 之间的随机查询
        queries = [random.randint(1, 2 * n) for _ in range(qnum)]
    else:
        assert len(queries) == qnum, "queries length must be qnum"

    l = arr[:]  # 复制，避免修改调用者的数组
    queries_cnt = qnum

    if queries_cnt == 0:
        return  # 不输出任何东西

    maxval = max(l)
    pairs = []
    count = 0
    f = l[0]
    secix = 1

    # 模拟直到最大值出现在数组头部
    while f != maxval:
        count += 1
        f = l[0]
        s = l[secix]
        pairs.append([f, s])
        f, s = max(f, s), min(f, s)
        l[0] = f
        l.append(s)
        secix += 1

    # 此时 l[0] == maxval
    l = [l[0]] + l[secix:]

    # 之后的对局为 maxval 与剩余元素的循环
    for i in range(n - 1):
        pairs.append([maxval, l[1 + i]])

    # 处理查询并输出
    for q in queries:
        if q <= count:
            a, b = pairs[q - 1]
        else:
            q -= (count + 1)
            pos = count + (q % (n - 1))
            a, b = pairs[pos]
        print(a, b)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)