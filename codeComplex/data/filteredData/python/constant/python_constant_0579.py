import random

def main(n: int):
    # 生成测试数据：棋盘大小为 n，随机生成一个位置 (x, y)
    # x, y 范围为 [1, n]
    x = random.randint(1, n)
    y = random.randint(1, n)

    d0 = max(x - 1, y - 1)
    d1 = max(n - x, n - y)
    result = 'White' if d0 <= d1 else 'Black'

    # 输出结果
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，指定规模 n
    main(8)