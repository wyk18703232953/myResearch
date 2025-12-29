import random

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main(n: int):
    # 1. 生成测试数据
    # 生成 n 个正整数作为 l，范围适当控制
    l = [random.randint(1, 10**6) for _ in range(n)]
    # 生成 n 个正整数作为 c，表示代价
    c = [random.randint(1, 10**6) for _ in range(n)]

    # 2. 原逻辑
    a = {0: 0}
    b = [0]

    for i in range(n):
        # 为避免在遍历过程中动态增长 b 带来的问题，固定当前长度
        current_b = list(b)
        for p in current_b:
            d = gcd(p, l[i])
            cost = a[p] + c[i]
            if d not in a:
                a[d] = cost
                b.append(d)
            elif a[d] > cost:
                a[d] = cost

    if 1 not in a:
        a[1] = -1

    # 输出结果（也可以选择 return）
    print(a[1])


if __name__ == "__main__":
    # 示例：调用 main，n 为规模
    main(5)