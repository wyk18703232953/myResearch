def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def prsh(N):
    prime = [2]
    for L in range(3, N):
        for p in prime:
            if not L % p:
                break
            if p > L ** 0.5:
                prime.append(L)
                break
    return prime


def main(n):
    """
    n: 规模，表示数组 A 的长度
    程序会根据 n 自动生成测试数据 A，并输出与原程序同样逻辑的结果。
    这里使用简单的测试数据生成方式：A = [1, 2, ..., n]
    """
    # 1. 生成测试数据 A（可按需要改成更复杂/随机的方式）
    A = list(range(1, n + 1))
    Ao = A[:]  # 保留原顺序
    A.sort()

    # 2. 按原程序构建可用的集合 C, Cp
    limit = 59
    prime = prsh(limit + 1)
    C = set([tuple()])
    Cp = []
    for i in range(2, limit + 1):
        if i >= 30 and i in prime:
            Cp.append(i)
            continue
        for k in C.copy():
            if all(gcd(ki, i) == 1 for ki in k):
                kn = tuple(list(k) + [i])
                C.add(kn)

    INF = 10 ** 9 + 7

    ans = INF
    Ans = None
    for ci in C:
        if len(ci) > n:
            continue
        # tc 至少需要长度 n + 7，原代码中最多访问到 tc[j + N - 1]，且 j 最多为 7
        base_len = n - len(ci)
        tc = [1] * base_len + list(ci) + Cp
        # 如果不够长，用 1 填充到 n + 7
        if len(tc) < n + 8:
            tc.extend([1] * (n + 8 - len(tc)))
        for j in range(8):
            res = 0
            for a, t in zip(A, tc[j:]):
                res += abs(a - t)
            if ans > res:
                ans = res
                Ans = tc[j:j + n]

    # 3. 按原逻辑还原到原顺序
    buc = [[] for _ in range(limit + 1)]
    for a, an in zip(A, Ans):
        if a <= limit:
            buc[a].append(an)

        else:
            # a 超过 limit 的情况，扩容 bucket
            while len(buc) <= a:
                buc.append([])
            buc[a].append(an)

    AA = []
    for ao in Ao:
        AA.append(buc[ao].pop())

    # 输出结果
    # print(*AA)
    pass


# 示例调用
if __name__ == "__main__":
    # 可修改为任意你想测试的 n
    main(5)