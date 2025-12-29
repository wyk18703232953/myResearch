import random

def if_Spruce(n, l, m):
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        if m[i] == 0:
            d[l[i]] += 1
    for i in range(1, n + 1):
        if m[i] > 0 and d[i] < 3:
            return "No"
    return "Yes"


def main(n):
    # 生成一棵以 1 为根的随机树
    l = [0] * 2           # 与原代码保持同样的前导长度
    m = [0] * (n + 1)

    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        l.append(parent)
        m[parent] += 1

    # 为了下标从 1 到 n 对齐，补齐 l 的长度
    # 原代码中 l 的有效部分是从索引 1 开始的父节点
    while len(l) <= n:
        l.append(0)

    result = if_Spruce(n, l, m)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)