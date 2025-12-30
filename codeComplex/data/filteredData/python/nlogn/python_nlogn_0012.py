from random import randint, uniform

def main(n):
    # 1. 生成测试数据
    # n 作为已有建筑的数量，将 new_width 固定或随机构造
    exist_num = n
    new_width = randint(1, 10)

    # 随机生成 exist_num 个建筑，使用中心坐标和宽度
    buildings = []
    for _ in range(exist_num):
        center = uniform(0, 100)
        width = uniform(1, 10)
        buildings.append((center - width / 2.0, center + width / 2.0))

    # 2. 按原逻辑处理
    buildings.sort()
    possible_loc = 2  # 两端各一个位置

    for left, right in zip(buildings, buildings[1:]):
        gap = right[0] - left[1]
        if gap == new_width:
            possible_loc += 1
        elif gap > new_width:
            possible_loc += 2

    print(possible_loc)


if __name__ == "__main__":
    # 示例调用
    main(5)