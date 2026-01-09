def main(n):
    d = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind",
    }

    all_colors = list(d.keys())

    # 根据 n 生成测试数据：取前 n 个颜色（若 n 超过可用数量，则截断）
    colors = all_colors[:max(0, min(n, len(all_colors)))]

    # print(len(d) - len(colors))
    pass
    for color in all_colors:
        if color not in colors:
            # print(d[color])
            pass
if __name__ == "__main__":
    # 示例：可修改这里的 n 测试不同规模
    main(3)