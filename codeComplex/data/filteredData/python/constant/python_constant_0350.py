def main(n):
    dic = {
        'purple': 'Power',
        'green': 'Time',
        'blue': 'Space',
        'orange': 'Soul',
        'red': 'Reality',
        'yellow': 'Mind'
    }

    # 根据 n 生成测试数据（前 n 个宝石颜色）
    colors = list(dic.keys())[:max(0, min(n, 6))]

    a = []
    for i in range(len(colors)):
        a.append(colors[i])

    # print(6 - len(a))
    pass
    for color in dic:
        if color not in a:
            # print(dic[color])
            pass
if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)