import random

def main(n):
    # 所有宝石颜色与名称映射
    d = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind"
    }

    colors = list(d.keys())
    # n 不能超过总数 6
    n = max(0, min(n, len(colors)))

    # 随机生成已拥有的颜色列表（模拟原来的输入）
    owned_colors = random.sample(colors, n)

    # 输出缺少的宝石数量
    print(len(colors) - n)

    # 按原字典顺序输出缺少的宝石名称
    for color in d:
        if color not in owned_colors:
            print(d[color])

if __name__ == "__main__":
    # 示例调用，可修改 n 来测试不同规模
    main(3)