from math import sin, tan, cos
import random


def main(n: int):
    """
    n 为规模参数，这里用于控制生成数据的范围（绝对值 < n）。
    生成一组 (x, y, z, t1, t2, t3)，然后按照原逻辑输出 YES 或 NO。
    """
    # 根据 n 生成测试数据（可按需修改生成策略）
    limit = max(1, n)  # 防止 n <= 0
    x = random.randint(-limit, limit)
    y = random.randint(-limit, limit)
    z = random.randint(-limit, limit)
    t1 = random.randint(1, limit)
    t2 = random.randint(1, limit)
    t3 = random.randint(1, limit)

    if abs(x - z) * t2 + abs(x - y) * t2 + 3 * t3 <= abs(x - y) * t1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)