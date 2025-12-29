import random

def main(n):
    # 生成一棵有 n 个节点的树（节点编号 1..n，1 为根）
    # arr[i] 表示节点 i+2 的父亲
    if n <= 1:
        print(1 if n == 1 else "")
        return

    # 随机生成父节点数组：对每个节点 2..n，随机选一个在 [1, i-1] 的父亲
    arr = [random.randint(1, i) for i in range(1, n)]

    children = [[] for _ in range(n + 1)]
    for i, j in enumerate(arr):
        if 1 < i + 2 <= n:
            children[j].append(i + 2)

    leaves = [0] * (n + 1)

    for i in range(n, 0, -1):
        if not children[i]:
            leaves[i] = 1
        else:
            leaves[i] = sum(leaves[j] for j in children[i])

    print(' '.join(map(str, sorted(leaves[1:]))))


if __name__ == "__main__":
    # 示例：可以在此处修改 n 进行测试
    main(10)