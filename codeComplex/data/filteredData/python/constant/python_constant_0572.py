import random

def main(n: int):
    # 根据规模 n 生成一组测试数据 (x, y)
    # 保证 1 <= x, y <= n
    x = random.randint(1, n)
    y = random.randint(1, n)

    white = max(x - 1, y - 1)
    black = max(n - x, n - y)
    print("White" if white <= black else "Black")


if __name__ == "__main__":
    # 示例：可在此处指定 n 进行测试
    main(8)