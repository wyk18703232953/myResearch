def distance(tree, outbreak):
    return abs(tree[0] - outbreak[0]) + abs(tree[1] - outbreak[1])


def shorthest_path(tree, outbreaks, min_dst):
    shorthest_path_val = float('inf')
    for outbreak in outbreaks:
        if shorthest_path_val < min_dst:
            break
        shorthest_path_val = min(shorthest_path_val, distance(tree, outbreak))
    return shorthest_path_val


def main(n):
    # 映射规模：
    # N, M 为网格大小；N = M = n
    # 构造若干个固定位置的爆发点，数量与 n 线性相关
    N = n
    M = n

    outbreaks = []
    if n <= 1:
        # 至少保证一个爆发点在 (1,1)，以避免空列表
        outbreaks.append((1, 1))

    else:
        # 确定性构造爆发点：在网格中均匀选取若干点
        # 数量设为 max(1, n // 2)，位置使用简单算术构造
        k = max(1, n // 2)
        for i in range(k):
            x = (i * 2) % N + 1
            y = (i * 3) % M + 1
            outbreaks.append((x, y))

    last_tree = (1, 1)
    best_dst = 0
    for x in range(1, N + 1):
        for y in range(1, M + 1):
            path_len = shorthest_path((x, y), outbreaks, best_dst)
            if path_len > best_dst:
                last_tree = (x, y)
                best_dst = path_len

    # print(last_tree[0], last_tree[1])
    pass
if __name__ == "__main__":
    # 示例：规模 n = 100
    main(100)