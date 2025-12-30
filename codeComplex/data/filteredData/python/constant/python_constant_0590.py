import random

def main(n: int):
    # 随机生成棋子位置 (x, y)，1 <= x, y <= n
    x = random.randint(1, n)
    y = random.randint(1, n)

    d1 = max(x - 1, y - 1)
    d2 = max(n - x, n - y)

    if d1 <= d2:
        print("White")
    else:
        print("Black")