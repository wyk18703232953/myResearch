import random

def main(n):
    # 1. 生成测试数据
    # 为了保证有意义的范围，构造 l 中元素为 1~100 的随机数
    l = [random.randint(1, 100) for _ in range(n)]
    # 令 ll、r 为根据 l 计算的范围，x 为一个随机差值
    total_sum = sum(l)
    ll = random.randint(0, max(0, total_sum // 2))
    r = random.randint(ll, total_sum)
    x = random.randint(0, max(l) - min(l) if n > 1 else 0)

    # 2. 原算法逻辑
    subset = []
    for i in range(1, (2 ** n)):
        sub = []
        for j in range(n):
            if (1 << j) & i > 0:
                sub.append(l[j])
        subset.append(sub)

    c = 0
    for i in subset:
        if len(i) > 1:
            su = sum(i)
            if (ll <= su <= r) and ((max(i) - min(i)) >= x):
                c += 1

    # 输出与原程序一样的结果（只输出计数）
    print(c)


if __name__ == "__main__":
    # 示例：n=5，可根据需要修改
    main(5)