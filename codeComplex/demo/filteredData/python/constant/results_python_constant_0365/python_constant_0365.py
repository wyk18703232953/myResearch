def main(n):
    allcolor = ['purple', 'green', 'blue', 'orange', 'red', 'yellow']
    op = ['Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind']

    # 生成测试数据：取前 n 个颜色（若 n 超过总数，则截断）
    ipcolor = allcolor[:min(n, len(allcolor))]

    diff = list(set(allcolor) - set(ipcolor))
    # print(len(diff))
    pass
    for c in diff:
        # print(op[allcolor.index(c)])
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(3)