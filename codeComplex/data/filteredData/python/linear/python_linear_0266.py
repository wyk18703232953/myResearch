import random

def main(n):
    # 生成一个含 n 个节点的随机树（边列表）
    # 节点编号从 1 到 n
    if n <= 1:
        print("No")
        return

    edges = []
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges.append([u, v])

    # 下面是原 main() 的逻辑，输入换成上面生成的 edges
    deg = [0] * n
    for u, v in edges:
        deg[u - 1] += 1
        deg[v - 1] += 1

    coun = [0, deg.count(1), deg.count(2)]

    if n - coun[1] == 1:
        print(f'Yes\n{n - 1}')
        for x in edges:
            print(*x)

    elif coun[1] + coun[2] == n:
        print(f'Yes\n1')
        print(deg.index(1) + 1, n - deg[::-1].index(1))

    elif n - sum(coun) == 1:
        for i in range(n):
            if deg[i] > 2:
                print(f'Yes\n{deg[i]}')
                for j in range(n):
                    if deg[j] == 1:
                        print(i + 1, j + 1)
                return
        print('No')
    else:
        print('No')


if __name__ == '__main__':
    # 示例：运行规模为 10
    main(10)