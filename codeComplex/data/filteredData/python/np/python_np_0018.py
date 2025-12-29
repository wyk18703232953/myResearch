import random
from collections import defaultdict

def get_bit(x, i):
    return (x >> i) & 1

def main(n):
    # 生成测试数据：n x n 矩阵 a，浮点数
    # 仅使用上三角（i < j）和对应的下三角（j > i）会被访问
    a = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            # 生成对称或非对称都可以，这里示例为对称矩阵
            val = random.random()
            a[i][j] = val
            a[j][i] = val

    masks = defaultdict(float)
    big = (1 << n) - 1

    if n == 1:
        print(1.0)
        return

    # 初始化 masks
    for i in range(n):
        for j in range(i + 1, n):
            masks[big ^ (1 << j)] += a[i][j]
            masks[big ^ (1 << i)] += a[j][i]

    # 主循环
    for _ in range(2, n):
        tem = defaultdict(float)
        for msk in list(masks.keys()):
            for bit in range(n):
                if get_bit(msk, bit):
                    s = 0.0
                    for i in range(n):
                        if get_bit(msk, i):
                            s += a[i][bit]
                    tem[msk ^ (1 << bit)] += s * masks[msk]
        masks = tem

    su = sum(masks.values())
    if su == 0:
        # 避免除零，如果 su 为 0，输出全 0
        res = [0.0] * n
    else:
        res = [masks[1 << i] / su for i in range(n)]

    print(*res)


if __name__ == "__main__":
    # 示例：调用 main(4)
    main(4)