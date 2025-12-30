import random

def f(lst, num):
    new = lst[num:] + lst[:num]
    return new

def main(n):
    """
    n 用作规模参数，这里用来生成测试数据：
    - 测试组数 t = n
    - 每组的 row, col 在 1~min(4, n) 之间随机生成
    - 每个元素在 0~9 之间随机生成
    """
    t = n

    for _ in range(t):
        # 生成行列数，保证不超过 4（原算法只轮转前 4 列）
        row = random.randint(1, min(4, max(1, n)))
        col = random.randint(1, min(4, max(1, n)))

        # 生成矩阵数据：row x col
        matrix = [[random.randint(0, 9) for _ in range(col)] for _ in range(row)]

        # 转换为原代码中的 lst 结构：每一列是一个列表
        # lst[k] 是第 k 列（长度为 row）
        lst = [[matrix[r][c] for r in range(row)] for c in range(col)]

        # 如果列数不足 4，补零列，使后续逻辑统一处理
        for _c in range(4 - col):
            lst.append([0] * row)

        # 按每列的最大值排序（降序）
        lst.sort(key=lambda x: max(x), reverse=True)

        ans = float('-inf')
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        if col >= 1:
                            aa = f(lst[0], a)
                        else:
                            aa = [0] * row
                        if col >= 2:
                            bb = f(lst[1], b)
                        else:
                            bb = [0] * row
                        if col >= 3:
                            cc = f(lst[2], c)
                        else:
                            cc = [0] * row
                        if col >= 4:
                            dd = f(lst[3], d)
                        else:
                            dd = [0] * row

                        tmp = 0
                        for j in range(row):
                            tmp += max(aa[j], bb[j], cc[j], dd[j])
                        ans = max(ans, tmp)

        print(ans)


if __name__ == "__main__":
    # 示例：规模参数 n = 3，可按需修改
    main(3)