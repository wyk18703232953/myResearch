def main(n):
    import random

    # 生成测试数据
    # 随机生成 m, k
    m = n  # 这里令 m = n，也可以按需求修改
    # 保证 k 为偶数，以避免整张为 -1 的特例；如需测试该特例，可改成随机奇偶
    k = random.randint(2, 10)
    if k % 2 == 1:
        k += 1

    # H: n 行, 每行 m-1 个数
    # V: n-1 行, 每行 m 个数
    # 边权使用 1~9 的随机正整数
    H = [[random.randint(1, 9) for _ in range(m - 1)] for _ in range(n)]
    V = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]

    # 若 k 为奇数，按照原逻辑输出全 -1
    if k & 1:
        ans = [['-1'] * m for _ in range(n)]
        return ans

    # DP 部分，和原始代码逻辑一致（只是去掉了输入和打印）
    d = [0] * (n * m)
    for _ in range(k // 2):
        nd = [0] * (n * m)
        for x in range(n):
            for y in range(m):
                v = x * m + y
                w = []
                if x:
                    w.append(d[v - m] + V[x - 1][y])
                if y:
                    w.append(d[v - 1] + H[x][y - 1])
                if x < n - 1:
                    w.append(d[v + m] + V[x][y])
                if y < m - 1:
                    w.append(d[v + 1] + H[x][y])
                nd[v] = min(w)
        d = nd

    # 生成结果矩阵（每个值乘以 2），与原代码输出形式一致
    result = [[str(2 * d[i * m + j]) for j in range(m)] for i in range(n)]
    return result


# 示例调用与打印（在线评测时可去掉以下示例）
if __name__ == "__main__":
    n = 4
    res = main(n)
    for row in res:
        print(' '.join(row))