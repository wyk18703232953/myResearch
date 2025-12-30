import random

def main(n: int):
    # 生成测试数据：在 [1, n] x [1, n] 的棋盘上随机选一个点 (x, y)
    x = random.randint(1, n)
    y = random.randint(1, n)

    na = abs(x - 1) + abs(y - 1)
    nb = abs(n - x) + abs(n - y)
    if na <= nb:
        print("white")
    else:
        print("black")


if __name__ == "__main__":
    # 示例：可自行修改 n 测试
    main(8)