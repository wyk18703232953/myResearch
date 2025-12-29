import random

def check(prev, parent, curr, level, degrees, neighbors, k):
    if level == 0:
        return len(parent) == 1 and degrees[curr - 1] == 1, []
    checked = []
    for neighbor in neighbors[curr - 1]:
        if len(prev) != 0 and prev[0] == neighbor:
            checked.append(neighbor)
            continue
        if len(parent) != 0 and parent[0] == neighbor:
            continue
        result, garbage = check([], [curr], neighbor, level - 1, degrees, neighbors, k)
        if result:
            checked.append(neighbor)
        else:
            if len(parent) == 0:
                parent.append(neighbor)
            else:
                return False, []
    if len(checked) > 2 and len(parent) == 0 and level == k:
        return True, []
    elif len(checked) > 2 and len(parent) == 1 and level != k:
        return True, parent
    else:
        return False, []


def generate_tree(n):
    """
    生成一棵随机树（n个节点, 节点编号为 1..n）。
    返回边列表 edges = [(u,v), ...]
    """
    if n <= 1:
        return []
    parents = list(range(1, n + 1))
    random.shuffle(parents)
    edges = []
    for i in range(1, n):
        u = parents[i]
        v = parents[random.randint(0, i - 1)]
        edges.append((u, v))
    return edges


def main(n):
    # 生成参数 k 和测试数据：
    # 约束：1 <= k < n，若 n <= 2，则令 k = 1
    if n <= 2:
        k = 1
    else:
        k = random.randint(1, n - 1)

    # 生成一棵有 n 个节点的随机树
    edges = generate_tree(n)

    # 构造 degrees 和 neighbors，与原程序保持一致
    degrees = [0] * n
    neighbors = [[] for _ in range(n)]
    for first, second in edges:
        degrees[first - 1] += 1
        degrees[second - 1] += 1
        neighbors[first - 1].append(second)
        neighbors[second - 1].append(first)

    # 以下为原主逻辑（去掉 input）
    curr = 0
    for i in range(n):
        if degrees[i] == 1:
            curr = i + 1
            break
    if curr == 0 or len(neighbors[curr - 1]) == 0:
        print("No")
        return
    curr = neighbors[curr - 1][0]

    prev = []
    parent = []
    counter = 1
    while counter <= k:
        result, parent = check(prev, [], curr, counter, degrees, neighbors, k)
        if not result:
            print("No")
            return
        if counter == k:
            print("Yes")
            return
        prev = [curr]
        curr = parent[0]
        counter += 1


if __name__ == "__main__":
    # 示例：用 n=10 运行一次
    main(10)