def main(n):
    # n 不再作为原来的单个整数使用，而是用于控制测试数据规模
    # 这里构造三个点 (x1, y1), (x2, y2), (x3, y3)
    # 让坐标与 n 相关且确定性生成
    x1 = n
    y1 = n // 2

    # 第二个点随 n 线性变化
    x2 = n + 1
    y2 = n + 2

    # 第三个点通过简单算术构造
    x3 = n * 2
    y3 = n * 2 + 1

    if (x2 < x1 and x3 < x1 or x2 > x1 and x3 > x1) and (y2 < y1 and y3 < y1 or y2 > y1 and y3 > y1):
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)