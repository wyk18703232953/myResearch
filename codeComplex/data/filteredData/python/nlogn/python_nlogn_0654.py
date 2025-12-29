import random

def main(n):
    # 生成测试数据：构造一个随机度序列 a，代表 n 个点的度数
    # 确保 sum(a) 为偶数，且存在至少一个点度数 > 1（否则原程序直接输出 NO）
    if n < 3:
        # 原代码假设 n >= 3；此处给一个简单例子
        a = [1] * n
    else:
        # 生成一个随机树或类似树的度分布：
        # 先构造一棵随机树的度数，再随机增添一些度数（仍保持总和为偶数）
        # 从而保证至少存在一个度数 > 1
        deg = [1] * n
        # 随机生成一棵树的度数（n-2 次给随机点加1度）
        for _ in range(n - 2):
            deg[random.randrange(n)] += 1

        # 可选：再随机增加一些度数，保证总体仍然是合理的度分布
        extra = random.randint(0, n // 2)
        for _ in range(extra):
            deg[random.randrange(n)] += 2  # 加2保持总和为偶数

        a = deg

    # 以下为原逻辑，去掉 input()，使用生成的 a 数组
    leafs = set()
    other = {}
    other_indices = []
    s = 0
    for i, val in enumerate(a):
        if val == 1:
            leafs.add(i)
        else:
            other[i] = val
            other_indices.append(i)
        s += val

    if not other:
        # n >= 3
        print("NO")
        return

    other_indices.sort(key=lambda index: other[index])
    other_indices = [other_indices[-1]] + other_indices[:-1]

    edges = []
    for i1, i2 in zip(other_indices, other_indices[1:]):
        edges.append((i1, i2))
        other[i1] -= 1
        if other[i1] == 0:
            del other[i1]
        other[i2] -= 1
        if other[i2] == 0:
            del other[i2]

    diam = len(other_indices) + min(2, len(leafs))

    has_start = has_end = False

    while leafs:
        if len(other) == 0:
            print("NO")
            return
        l = leafs.pop()
        if not has_start and other.get(other_indices[0], 0):
            i = other_indices[0]
            has_start = True
        elif not has_end and other.get(other_indices[-1], 0):
            i = other_indices[-1]
            has_end = True
        else:
            i = next(iter(other))
        edges.append((l, i))
        other[i] -= 1
        if other[i] == 0:
            del other[i]

    print("YES", diam - 1)
    print(len(edges))
    for x, y in edges:
        print(x + 1, y + 1)


# 示例调用（提交到评测时可去掉或改为由外部调用）
if __name__ == "__main__":
    main(10)