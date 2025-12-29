from math import sqrt

def main(n):
    # 根据规模 n 生成测试数据
    # 这里生成 a = n 个圆心，半径 r = 1，x 为等差或简单序列
    r = 1
    a = n
    x = list(range(a))

    y = [0] * a
    result = []

    for i in range(a):
        h = r
        for j in range(i):
            if abs(x[i] - x[j]) <= 2 * r:
                h = max(h, sqrt((2 * r) ** 2 - (x[i] - x[j]) ** 2) + y[j])
        y[i] = h
        result.append(h)

    # 输出与原程序一致：同一行输出，空格分隔
    print(" ".join(str(v) for v in result))


if __name__ == "__main__":
    # 示例：n=5，可按需修改
    main(5)