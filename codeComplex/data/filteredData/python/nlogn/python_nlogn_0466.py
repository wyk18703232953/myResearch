import random

def main(n):
    # 生成测试数据：n 个整数，k 随机在 1..n 之间
    k = random.randint(1, n)
    a = [random.randint(1, 100) for _ in range(n)]

    b = list(a)
    b.sort()
    c = []
    total = 0
    for i in range(1, k + 1):
        c.append(b[-i])
        total += b[-i]
    print(total)

    d = []
    for i in range(n):
        if a[i] in c:
            d.append(i)
            c.remove(a[i])
        else:
            pass
    d.insert(0, -1)
    d[-1] = n - 1
    e = []
    for i in range(1, len(d)):
        e.append(d[i] - d[i - 1])
    print(" ".join(map(str, e)))


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)