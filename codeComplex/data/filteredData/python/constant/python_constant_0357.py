def main(n):
    # 字典：颜色 -> 宝石名
    d = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind"
    }

    # 根据 n 生成测试数据：取前 n 个颜色作为“已收集”的颜色
    # 若 n > 6，只取前 6 个，逻辑上等同于原题最多输入 6 行
    colors = list(d.keys())
    n = min(n, len(colors))
    collected = set(colors[:n])

    # 输出缺少的宝石数量
    print(6 - n)

    # 输出缺少的宝石名称
    for color, gem in d.items():
        if color not in collected:
            print(gem)


if __name__ == "__main__":
    # 示例运行：可修改这里的 n 做测试
    main(3)