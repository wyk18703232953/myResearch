import random

def main(n: int):
    # 生成一棵以 1 为根的随机树，节点编号 1..n
    # parent[i] 表示节点 i 的父节点（i>=2）
    parent = [0] * (n + 1)
    for i in range(2, n + 1):
        parent[i] = random.randint(1, i - 1)

    # 构建子节点字典 g：g[p] = [p 的所有子节点]
    g = {}
    for i in range(1, n):
        p = parent[i + 1]
        if p in g:
            g[p].append(i + 1)
        else:
            g[p] = [i + 1]

    ams = 'YES'
    for i in g:
        c = 0
        for j in g[i]:
            if j not in g:
                c += 1
        if c < 3:
            ams = 'NO'
            break

    print(ams)


if __name__ == "__main__":
    # 示例：n 可根据需要修改
    main(10)