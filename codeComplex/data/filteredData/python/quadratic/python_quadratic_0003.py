import math as m
import random

def main(n):
    # 生成测试数据：n 个圆盘，半径 r，x 坐标升序
    r = 1
    step = 2 * r  # 让圆盘大致首尾相接
    x = [i * step for i in range(n)]

    y = []
    for i in range(len(x)):
        tempY = [r]
        for j in range(i):
            diffX = abs(x[i] - x[j])
            if diffX <= (2 * r):
                addY = m.sqrt((4 * r * r) - (diffX * diffX))
                tempY.append(y[j] + addY)
        y.append(max(tempY))

    for yi in y:
        print(yi, end=' ')
    print()

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)