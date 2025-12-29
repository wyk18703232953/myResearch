import random

def main(n: int):
    # n 为已拥有的宝石数量，规模不超过 6
    dic = {
        'purple': 'Power',
        'green': 'Time',
        'blue': 'Space',
        'orange': 'Soul',
        'red': 'Reality',
        'yellow': 'Mind'
    }

    # 约束：实际最多只能有 6 颗不同颜色的宝石
    n = max(0, min(n, 6))

    # 根据 n 随机生成测试数据：从 6 种颜色中选 n 种
    colors = list(dic.keys())
    owned_colors = random.sample(colors, n)

    kol = n
    r = []
    g = []
    missing = 6 - kol

    # 原逻辑：将拥有的宝石颜色记录到 r 中
    for rocks in owned_colors:
        r.append(rocks)

    # 找出缺失的宝石对应的能力
    for key in dic:
        if r.count(key) == 0:
            g.append(dic[key])

    # 输出结果
    print(missing)
    for stone in g:
        print(stone)


if __name__ == "__main__":
    # 示例：调用 main(3)，可根据需要修改
    main(3)