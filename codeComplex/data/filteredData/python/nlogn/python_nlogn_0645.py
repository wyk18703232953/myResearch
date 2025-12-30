import random

def main(n):
    # 1) 生成测试数据
    #   n: 原代码中的 n
    #   m: 随机取一个与 n 同级别的规模（可根据需要调整策略）
    m = random.randint(1, max(1, n * 2))

    # 生成 y 列表（长度为 n）
    # 随机生成 1~1e9 范围内的整数
    y = [random.randint(1, 10**9) for _ in range(n)]
    y.append(10 ** 9)

    # 生成 (a, b, c) 共 m 条记录，其中 a==1 的会对逻辑产生影响
    # 为了使 x 不为空，给一定概率生成 a == 1 的记录
    triples = []
    for _ in range(m):
        # 让 a 为 1 的概率较大一些
        a = 1 if random.random() < 0.7 else random.randint(1, 3)
        b = random.randint(1, 10**9)
        c = random.randint(1, 10**9)
        triples.append((a, b, c))

    # 2) 按原逻辑构造 x
    x = []
    for a, b, c in triples:
        if a == 1:
            x.append(b)

    # 3) 按原程序逻辑进行计算
    y.sort()
    x.sort()
    m = len(x)
    ans = m
    k = 0

    for i in range(n + 1):
        ok = True
        for j in range(k, m):
            if y[i] <= x[j]:
                k = j
                ok = False
                break
        if ok:
            k = m
            ans = min(ans, m - k + i)
            break
        ans = min(ans, m - k + i)

    print(ans)


# 示例调用
if __name__ == "__main__":
    main(10)