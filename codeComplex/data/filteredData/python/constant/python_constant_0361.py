def main(n):
    # 全部宝石映射
    stone_map = {
        "Power": "purple",
        "Time": "green",
        "Space": "blue",
        "Soul": "orange",
        "Reality": "red",
        "Mind": "yellow"
    }

    # 根据 n 生成测试数据：取前 n 个颜色作为“已获得”的宝石颜色
    colors = list(stone_map.values())
    n = max(0, min(n, len(colors)))  # 限制 n 到 [0, 6]
    test_colors = colors[:n]

    obtained = {}
    for color in test_colors:
        if color == "purple":
            obtained["Power"] = color
        elif color == "green":
            obtained["Time"] = color
        elif color == "blue":
            obtained["Space"] = color
        elif color == "orange":
            obtained["Soul"] = color
        elif color == "red":
            obtained["Reality"] = color
        elif color == "yellow":
            obtained["Mind"] = color

    all_names = list(stone_map.keys())
    obtained_names = list(obtained.keys())
    missing = [name for name in all_names if name not in obtained_names]

    # print(len(missing))
    pass
    for name in missing:
        # print(name)
        pass
if __name__ == "__main__":
    # 示例：规模为 3，可自行修改
    main(3)