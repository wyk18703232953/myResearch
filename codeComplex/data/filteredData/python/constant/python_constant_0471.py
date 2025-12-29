import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里理解为：
    # 在平面上随机生成 3 个点 (ax, ay), (bx, by), (cx, cy)
    # n 用来控制坐标的范围 [-n, n]
    ax = random.randint(-n, n)
    ay = random.randint(-n, n)
    bx = random.randint(-n, n)
    by = random.randint(-n, n)
    cx = random.randint(-n, n)
    cy = random.randint(-n, n)

    if (ax - bx) * (ax - cx) > 0 and (ay - by) * (ay - cy) > 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main，规模参数可自行调整
    main(10)