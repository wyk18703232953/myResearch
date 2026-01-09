import math

def main(n):
    # 映射含义：
    #   n: 正多边形边数
    #   r: 固定为 n 的线性函数，保证随规模变化
    # 生成确定性数据
    sides = max(3, n)  # 至少为 3，避免无效几何
    r = float(sides * 2)  # 确定性的半径，随 n 线性增长

    angle = math.pi / sides
    s = math.sin(angle)
    result = r * s / (1 - s)
    # print('%.8f' % result)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)