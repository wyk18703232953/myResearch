import random

def main(n):
    # 1. 生成测试数据
    # 随机生成 k，范围 1..n
    k = random.randint(1, n)

    # 生成 p：取值范围 1..n 的随机排列（或可有重复，这里允许重复）
    p = [random.randint(1, n) for _ in range(n)]

    # 生成 c：取值范围 1..10^4
    c = [random.randint(1, 10**4) for _ in range(n)]

    # 2. 原逻辑
    m = {}
    for i in range(n):
        if p[i] not in m:
            m[p[i]] = []
        m[p[i]].append(c[i])

    a = {}
    t = []
    for key, val in sorted(m.items()):
        a[key] = sum(t)
        t += val
        t.sort()
        t = t[max(0, len(t) - k):len(t)]

    result = " ".join(str(a[p[i]] + c[i]) for i in range(n))
    print(result)
    return result

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)