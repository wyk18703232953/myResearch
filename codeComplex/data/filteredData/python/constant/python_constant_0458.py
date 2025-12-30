import random

def main(n: int):
    # 生成测试数据：三个点 (x1, y1), (x2, y2), (x3, y3)
    # n 作为坐标绝对值的最大范围
    x1, y1 = random.randint(-n, n), random.randint(-n, n)
    x2, y2 = random.randint(-n, n), random.randint(-n, n)
    x3, y3 = random.randint(-n, n), random.randint(-n, n)

    if ((x2 < x1 and x3 < x1) or (x2 > x1 and x3 > x1)) and \
       ((y2 < y1 and y3 < y1) or (y2 > y1 and y3 > y1)):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：可自行修改 n 的值进行测试
    main(10)