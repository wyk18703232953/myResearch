import random

def main(n: int):
    # 所有可能的宝石颜色
    all_colors = ["purple", "green", "blue", "orange", "red", "yellow"]
    li2 = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind"
    }

    # 根据 n 生成测试数据：从 6 个颜色中随机选 n 个不重复的颜色
    n = max(0, min(n, 6))  # 保证 0 <= n <= 6
    li1 = random.sample(all_colors, n)

    # 原逻辑：输出缺少的宝石数量
    print(6 - n)

    # 按原程序对 li2 遍历顺序，输出缺失宝石对应的名称
    for key in li2:
        if key in li1:
            continue
        else:
            li1.append(key)
            print(li2[key])


if __name__ == "__main__":
    # 示例调用：可根据需要修改规模 n
    main(3)