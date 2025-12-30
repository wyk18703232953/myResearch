import random

def main(n):
    # 生成一棵规模为 n 的树的父节点数组 p（1 为根）
    # p[1] = 0，p[2..n] 为 1..i-1 中的一个，保证是树
    p = [0, 0]  # 占位，使得节点从 1 开始
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
    # 示例：调用 main(5)
    main(5)