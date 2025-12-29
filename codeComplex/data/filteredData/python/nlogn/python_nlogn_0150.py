import random

def main(n):
    # 生成测试数据：
    # 固定 k >= 2，随机选择
    k = random.randint(2, 5)

    # 生成 n 个正整数，尽量包含一些成倍关系，模仿原逻辑的作用场景
    a = []
    for _ in range(n):
        # 生成基数，并有一定概率乘以 k 或 k^2 来制造链式关系
        base = random.randint(1, 2 * n)
        r = random.random()
        if r < 0.3:
            val = base * k
        elif r < 0.4:
            val = base * k * k
        else:
            val = base
        a.append(val)

    # 原始逻辑开始
    if k == 1:
        print(n)
        return

    a.sort()

    # 将值映射为 0..n-1（与原代码行为一致）
    c = dict(zip(a, range(n)))
    a = c  # a 变为字典：值 -> 下标（但后续仅把键当作原来的值来迭代）

    b = {}
    count = {}

    for x in a:
        if x % k == 0 and int(x / k) in a:
            b[x] = b[int(x / k)]
            count[b[int(x / k)]] += 1
        else:
            b[x] = x
            count[x] = 1

    ans = n
    for _, y in count.items():
        ans -= int(y / 2)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)