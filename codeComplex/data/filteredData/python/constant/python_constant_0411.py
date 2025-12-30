def sol(a, b):
    for square in [a, b]:
        for i1 in range(4):
            i2 = (i1 + 1) % 4
            p1, p2 = square[i1], square[i2]

            norm = (p2[1] - p1[1], p1[0] - p2[0])

            minA = maxA = minB = maxB = None
            for p in a:
                proj = norm[0] * p[0] + norm[1] * p[1]
                if minA is None or proj < minA:
                    minA = proj
                if maxA is None or proj > maxA:
                    maxA = proj
            for p in b:
                proj = norm[0] * p[0] + norm[1] * p[1]
                if minB is None or proj < minB:
                    minB = proj
                if maxB is None or proj > maxB:
                    maxB = proj

            if maxA < minB or maxB < minA:
                return False
    return True


def main(n):
    """
    n 为规模参数，用于生成两组测试数据：
    - 第一组：以原点为中心，边长 n 的轴对齐正方形
    - 第二组：以 (n, n) 为中心，边长 n/2 的旋转 45 度的正方形
    """
    # 轴对齐正方形 a：中心在 (0,0)，边长 n
    half_n = n / 2.0
    a = [
        (-half_n, -half_n),
        (half_n, -half_n),
        (half_n, half_n),
        (-half_n, half_n),
    ]

    # 旋转 45 度正方形 b：中心 (n, n)，边长 n/2
    import math
    side_b = n / 2.0
    half_b = side_b / math.sqrt(2)  # 对于旋转 45 度，中心到顶点距离
    cx, cy = n, n
    b = [
        (cx - half_b, cy),
        (cx, cy + half_b),
        (cx + half_b, cy),
        (cx, cy - half_b),
    ]

    result = ["NO", "YES"][sol(a, b)]
    print(result)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)