import random

def main(n):
    # 所有颜色与宝石映射
    color_to_gem = {
        'purple': 'Power',
        'green': 'Time',
        'blue': 'Space',
        'orange': 'Soul',
        'red': 'Reality',
        'yellow': 'Mind'
    }
    all_colors = list(color_to_gem.keys())
    
    # 生成测试数据：随机选择 n 个颜色（允许重复）
    test_colors = [random.choice(all_colors) for _ in range(n)]
    
    # 原逻辑
    s = ['Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind']
    for color in test_colors:
        gem = color_to_gem[color]
        if gem in s:
            s.remove(gem)
    
    print(len(s))
    for gem in s:
        print(gem)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(3)