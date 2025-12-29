import random

def quadrant(x, y, rx, ry):
    if x > rx and y > ry:
        return 1
    elif x < rx and y > ry:
        return 2
    elif x < rx and y < ry:
        return 3
    else:
        return 4

def main(n):
    random.seed(n)
    # 根据规模 n 生成测试数据，这里仅用 n 作为坐标范围上界
    limit = max(1, n)

    qx = random.randint(-limit, limit)
    qy = random.randint(-limit, limit)
    kx = random.randint(-limit, limit)
    ky = random.randint(-limit, limit)
    cx = random.randint(-limit, limit)
    cy = random.randint(-limit, limit)

    if quadrant(kx, ky, qx, qy) == quadrant(cx, cy, qx, qy):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值
    main(10)