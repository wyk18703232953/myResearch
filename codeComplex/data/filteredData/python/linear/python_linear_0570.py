import random

def main(n: int):
    # 生成一个父节点数组 p，表示一棵有 n 个节点、根为 1 的树
    # p[1] 无父节点，记为 0；对于 i >= 2，1 <= p[i] < i，保证形成一棵树
    p = [0, 0]
    for i in range(2, n + 1):
        p.append(random.randint(1, i - 1))

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
    # 示例：调用 main(10)，可根据需要修改规模 n
    main(10)