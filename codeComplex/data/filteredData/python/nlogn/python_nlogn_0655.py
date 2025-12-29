import random

def main(n):
    # 生成测试数据：长度为 n 的度数列表（保证度数 >= 1，且尽量可构造）
    # 这里简单生成：每个度数在 [1, max(1, n-1)] 之间
    # 并做一次调整避免明显不合法（如所有度数为 1 且 n > 2 时不变，这恰好对应原程序的 NO 分支之一）
    degs = [random.randint(1, max(1, n - 1)) for _ in range(n)]

    # 下面是将原 main() 逻辑改为使用自动生成的 degs 列表

    a = []
    for i, d in enumerate(degs):
        a.append([i + 1, int(d)])

    a = list(reversed(list(sorted(a, key=lambda x: x[1]))))
    one_deg_count = 0
    for i in a:
        if i[1] == 1:
            one_deg_count += 1

    if one_deg_count == len(a):  # only 1-degree vertices
        if one_deg_count == 2:
            print("YES", 1)  # result, diameter
            print(1)  # edge count
            print(1, 2)  # edge info
        else:
            print("NO")
        return
    elif one_deg_count == len(a) - 1:  # one multi-degree vertex and n-1 1-degree vertices
        if one_deg_count <= a[0][1]:
            print("YES", 2)  # star-shaped graph
            print(one_deg_count)
            for i in range(one_deg_count):
                print(a[0][0], a[-i - 1][0])
        else:
            print("NO")
        return
    else:  # more than one multi-degree vertices
        spare_edges = 2
        for i in range(len(a) - one_deg_count):
            spare_edges += a[i][1] - 2
        if spare_edges >= one_deg_count:
            diameter = len(a) - 1 - one_deg_count + min(one_deg_count, 2)
            edge_list = []
            # 链接多度顶点成一条链
            for i in range(len(a) - one_deg_count - 1):
                edge_list.append((a[i][0], a[i + 1][0]))
            for i in range(len(a) - one_deg_count):
                a[i][1] -= 2
            # 处理度为 1 的顶点
            if one_deg_count > 0:
                edge_list.append((a[0][0], a[-1][0]))
                one_deg_count -= 1
            if one_deg_count > 0:
                edge_list.append((a[-one_deg_count - 2][0], a[-2][0]))
                one_deg_count -= 1
            idx = 0
            for i in range(one_deg_count):
                edge_list.append((a[idx][0], a[-i - 3][0]))
                a[idx][1] -= 1
                if a[idx][1] <= 0:
                    idx += 1
            print("YES", diameter)
            print(len(edge_list))
            for u, v in edge_list:
                print(u, v)
        else:
            print("NO")  # impossible


if __name__ == '__main__':
    # 示例：调用 main(5)
    main(5)