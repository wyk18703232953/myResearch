import random

def main(n: int):
    # n 作为规模，这里用来控制随机数范围
    # 随机生成 A(ax, ay), B(bx, by), C(cx, cy)
    limit = max(1, n)
    ax = random.randint(-limit, limit)
    ay = random.randint(-limit, limit)
    bx = random.randint(-limit, limit)
    by = random.randint(-limit, limit)
    cx = random.randint(-limit, limit)
    cy = random.randint(-limit, limit)

    if bx < ax < cx:
        print("NO")
    elif cx < ax < bx:
        print("NO")
    elif by < ay < cy:
        print("NO")
    elif cy < ay < by:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)