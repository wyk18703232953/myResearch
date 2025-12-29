def main(n):
    # 所有宝石
    d = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind"
    }

    # 根据 n 生成测试数据：取前 n 个颜色名作为“已收集”的宝石
    # 若 n > 6，则只取前 6 个（避免越界）
    colors = list(d.keys())
    n = min(n, len(colors))
    collected = set(colors[:n])

    # 输出缺少的宝石数量
    print(6 - n)

    # 输出缺少的宝石名称
    for key, value in d.items():
        if key not in collected:
            print(value)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行测试
    main(3)