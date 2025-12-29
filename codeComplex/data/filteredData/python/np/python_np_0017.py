import random

class dict_with_default(dict):
    def __missing__(self, key):
        return 0

def get_bit(x, i):
    return (x >> i) & 1

def main(n):
    # 1. 生成测试数据 a：n x n 的浮点矩阵，这里生成随机非负数
    # 根据原代码使用 a[i][j] 和 a[j][i]，不需要对角线，设为 0
    random.seed(0)
    a = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                a[i][j] = random.random()

    masks = dict_with_default()
    big = (1 << n) - 1  # 2**n - 1

    if n == 1:
        print(1.0)
        return

    # 原始逻辑
    for i in range(n):
        for j in range(i + 1, n):
            masks[big ^ (1 << j)] += a[i][j]
            masks[big ^ (1 << i)] += a[j][i]

    for _ in range(2, n):
        tem = dict_with_default()
        for msk in masks:
            for bit in range(n):  # 原代码固定 18，这里用 n 以适配规模
                if get_bit(msk, bit):
                    s = 0.0
                    for i in range(n):
                        if get_bit(msk, i):
                            s += a[i][bit]
                    tem[msk ^ (1 << bit)] += s * masks[msk]
        masks = tem

    su = sum(masks.values())
    if su == 0:
        # 避免除零，退化为均匀分布
        res = [1.0 / n] * n
    else:
        res = [masks[1 << i] / su for i in range(n)]
    print(*res)


if __name__ == "__main__":
    # 示例：运行规模为 4
    main(4)