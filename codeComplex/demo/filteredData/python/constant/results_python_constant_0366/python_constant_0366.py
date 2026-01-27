def main(n):
    d = {
        'purple': 'Power',
        'green': 'Time',
        'blue': 'Space',
        'orange': 'Soul',
        'red': 'Reality',
        'yellow': 'Mind'
    }
    colors = ['purple', 'green', 'blue', 'orange', 'red', 'yellow']
    # 确定性生成要删除的颜色序列：按顺序循环删除前 n 个
    remove_order = [colors[i % len(colors)] for i in range(n)]
    for color in remove_order:
        d.pop(color, None)
    # 收集输出结果，返回而不是直接打印，便于实验使用
    remaining = list(d.values())
    return len(d), remaining


if __name__ == "__main__":
    # 示例：以 n = 3 运行
    count, stones = main(3)
    # print(count, *stones, sep="\n")
    pass