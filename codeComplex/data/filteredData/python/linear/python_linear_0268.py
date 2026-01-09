def main(n):
    # 生成测试数据：构造一棵 n 个点的树，边存为 (u, v) 列表
    # 这里给出一种简单的生成方式，可以按需要修改：
    edges = []
    if n == 1:
        # 原逻辑中 n>=2 才有意义，这里 n=1 时直接返回
        # print("No")
        pass
        return
    elif n == 2:
        edges.append((1, 2))

    else:
        # 生成一棵“星形”树：1 与 2..n 相连
        # 这样 1 的度最大，且叶子最多，便于测试逻辑
        for v in range(2, n + 1):
            edges.append((1, v))

    # --------- 以下为对原 main() 逻辑的等价实现 ---------
    deg = [0] * n
    if n == 2:
        # 原程序在读完 n 和一条边后就直接输出固定答案
        # 这里按原逻辑输出
        # print("Yes")
        pass
        # print(1)
        pass
        # print("1 2")
        pass
        return

    for u, v in edges:
        deg[u - 1] += 1
        deg[v - 1] += 1

    ix = deg.index(max(deg))

    if deg[ix] < 3 or deg.count(1) + deg.count(2) == n - 1:
        # print("Yes")
        pass
        # print(deg.count(1))
        pass
        for i in range(n):
            if deg[i] == 1:
                # print(i + 1, ix + 1)
                pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)