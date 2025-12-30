import random

def main(n: int):
    # 生成测试数据：棋盘大小为 n，随机生成 1~n 内的坐标 (x, y)
    x = random.randint(1, n)
    y = random.randint(1, n)

    # 原逻辑
    if x - 1 + y - 1 <= n - x + n - y:
        print('White')
    else:
        print('Black')

if __name__ == "__main__":
    # 示例：可根据需要修改 n 的值
    main(8)