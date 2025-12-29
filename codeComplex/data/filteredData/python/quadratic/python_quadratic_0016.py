import random
import math

def main(n):
    # 参数设置：半径 r，可根据需要调整或改为函数参数
    r = 10

    # 生成测试数据：n 个整数坐标，这里简单生成非降序随机坐标
    # 这样更符合原题中常见的“顺序放置气球/圆”的场景
    x_coord = []
    cur = 0
    for _ in range(n):
        cur += random.randint(0, r * 2)  # 控制相邻点距离
        x_coord.append(cur)

    d = {}
    results = []
    for i in x_coord:
        final = r
        for j in range(i - r, i + r + 1):
            check = d.get(j, [-1, -1])
            if check[0] > 0:
                potential = check[1] + math.sqrt((4 * r * r) - ((i - check[0]) ** 2))
                final = max(potential, final)
        for j in range(i - r, i + r + 1):
            d[j] = (i, final)
        results.append(final)

    # 按原程序风格输出到标准输出
    print(" ".join(str(v) for v in results))


# 示例：当本文件直接运行时，使用一个默认规模
if __name__ == "__main__":
    main(5)