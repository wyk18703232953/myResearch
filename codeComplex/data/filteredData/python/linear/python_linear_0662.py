import random

def main(n):
    # 根据 n 生成树结构与 s
    # 生成一个随机树：节点 1..n
    v = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        v[parent].append(i)
        v[i].append(parent)

    # 生成 s（可按需要调整范围）
    s = random.randint(1, 10**6)

    # 计算叶子数量
    leaf_count = 0
    for i in range(1, n + 1):
        if len(v[i]) == 1:
            leaf_count += 1

    # 原逻辑：输出 2*s/叶子数
    result = 2 * s / leaf_count if leaf_count > 0 else 0
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)