def main(n):
    # 颜色与宝石的对应关系
    color = ['purple', 'green', 'blue', 'orange', 'red', 'yellow']
    gem = ['Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind']

    # 根据规模 n 自动生成测试数据：
    # 取前 n 个颜色作为“已给出的颜色”
    # 即模拟输入中给出了这 n 个颜色
    given_colors = color[:n]

    # 模拟原逻辑：移除已经出现的颜色对应的宝石
    remaining_colors = color[:]
    remaining_gems = gem[:]

    for s in given_colors:
        indexofcolor = remaining_colors.index(s)
        remaining_colors.pop(indexofcolor)
        remaining_gems.pop(indexofcolor)

    # 输出与原程序一致
    print(len(remaining_gems))
    for g in remaining_gems:
        print(g)


if __name__ == "__main__":
    # 示例调用：这里可修改 n 来测试不同规模
    main(3)