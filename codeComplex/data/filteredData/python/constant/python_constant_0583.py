import random

def main(n: int):
    # 生成测试数据：在 n x n 棋盘上随机选一个点 (x, y)
    # 坐标范围为 1..n
    x = random.randint(1, n)
    y = random.randint(1, n)

    # 原逻辑：比较该点到左上角(1,1)和右下角(n,n)的曼哈顿距离
    d1 = abs(1 - x) + abs(1 - y)
    d2 = abs(n - x) + abs(n - y)

    # 输出结果
    if d1 <= d2:
        print('White')
    else:
        print('Black')


if __name__ == "__main__":
    # 示例：规模 n = 8（可以根据需要修改或在外部调用 main(n)）
    main(8)