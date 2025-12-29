import random

def main(n: int):
    # 生成测试数据：p[2..n] 为一棵以 1 为根的树的父节点数组
    if n == 1:
        p = [0, 0]  # p[1] 不使用，这里占位
    else:
        p = [0, 0]
        # 对于 i 从 2 到 n，随机选择 [1, i-1] 之间的一个作为父节点，保证为树
        for i in range(2, n + 1):
            parent = random.randint(1, i - 1)
            p.append(parent)

    d = [0] * (n + 1)

    for i in range(n, 1, -1):
        if d[i] == 0:
            d[i] = 1
        d[p[i]] += d[i]

    if n == 1:
        d[1] = 1

    d = d[1:]
    d.sort()

    print(*d)


if __name__ == "__main__":
    # 示例：运行 main(10)，可按需修改 n
    main(10)