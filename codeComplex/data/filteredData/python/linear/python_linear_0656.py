from collections import Counter
import random

def main(n):
    # 随机生成总长度 s（正数）
    s = random.uniform(1.0, 1000.0)

    # 生成一棵有 n 个节点的随机树，节点编号为 1..n
    # 使用简单的随机生成方法：对每个节点 i (2..n)，连到 [1..i-1] 中的随机节点
    d = Counter()
    edges = []
    for i in range(2, n + 1):
        p = random.randint(1, i - 1)
        edges.append((p, i))
        d[p] += 1
        d[i] += 1

    # 如果 n == 1，则只有一个节点，按原题意义没有边，叶子数视为 1
    if n == 1:
        l = 1
    else:
        l = sum(deg == 1 for deg in d.values())

    ans = s / l * 2
    print(f"{ans:.10f}")

if __name__ == "__main__":
    # 示例：运行规模为 5 的随机测试
    main(5)