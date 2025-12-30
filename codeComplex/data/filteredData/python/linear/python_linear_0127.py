import random

def if_spruce(n, l, s):
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        if i not in s:          # i 是叶子
            d[l[i]] += 1        # 统计其父节点的叶子数量
    for i in range(1, n + 1):
        if i in s and d[i] < 3: # i 是内部节点但叶子孩子少于 3
            return "No"
    return "Yes"


def main(n):
    # 生成一棵有 n 个节点的树，父节点数组 l 从索引 1 开始
    # 保证是棵树：对每个节点 i (2..n)，随机连到 1..i-1 的某个节点
    l = [0, 0]  # 占位：l[0] 无用，l[1]=0 表示根没有父亲
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        l.append(parent)

    s = set(l)  # 出现在父数组中的都是内部节点（非叶子）
    print(if_spruce(n, l, s))


if __name__ == "__main__":
    # 示例：可修改 n 测试不同规模
    main(10)