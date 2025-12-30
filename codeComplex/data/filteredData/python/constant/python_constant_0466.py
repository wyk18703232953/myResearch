import random

def main(n: int):
    # 生成测试数据：
    # 为了体现“规模 n”，这里生成坐标在 [-n, n] 范围内的三个点
    ax, ay = random.randint(-n, n), random.randint(-n, n)
    bx, by = random.randint(-n, n), random.randint(-n, n)
    cx, cy = random.randint(-n, n), random.randint(-n, n)

    # 原始逻辑
    if (bx < ax < cx) or (bx > ax > cx) or (by < ay < cy) or (by > ay > cy):
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)