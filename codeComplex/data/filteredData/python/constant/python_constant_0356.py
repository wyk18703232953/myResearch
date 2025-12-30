def main(n):
    # 根据 n 生成测试数据，这里示例为取前 n 个宝石名称作为输入
    all_gem_names = ['purple', 'green', 'blue', 'orange', 'red', 'yellow']
    gems_in = all_gem_names[:n]

    gems = {
        'purple': 'Power',
        'green': 'Time',
        'blue': 'Space',
        'orange': 'Soul',
        'red': 'Reality',
        'yellow': 'Mind'
    }

    print(6 - len(gems_in))
    r = list(set(gems) - set(gems_in))
    for gem in r:
        print(gems[gem])


if __name__ == "__main__":
    # 示例：调用 main(3)，可根据需要修改
    main(3)