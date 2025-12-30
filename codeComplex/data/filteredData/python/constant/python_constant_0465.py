import random

def main(n: int):
    # 随机生成点 A, B, C 的坐标，坐标范围可随 n 调整
    # 这里示例取范围 [-n, n]
    ax = random.randint(-n, n)
    ay = random.randint(-n, n)
    bx = random.randint(-n, n)
    by = random.randint(-n, n)
    cx = random.randint(-n, n)
    cy = random.randint(-n, n)

    # 原逻辑
    if (bx > ax, by > ay) != (cx > ax, cy > ay):
        print("NO")
        return

    print("YES")


if __name__ == "__main__":
    # 示例：n 可根据需要修改或由外部调用 main(n)
    main(10)