import random

def main(n: int):
    # 生成测试数据：
    # 固定 q 在 (0,0)，随机生成 k 和 dest，坐标范围随 n 放大
    global q_x, q_y
    q_x, q_y = 0, 0

    coord_range = n if n > 0 else 1
    k_x = random.randint(-coord_range, coord_range)
    k_y = random.randint(-coord_range, coord_range)
    dest_x = random.randint(-coord_range, coord_range)
    dest_y = random.randint(-coord_range, coord_range)

    def sign(x):
        return 1 if x >= 0 else -1

    def which_square(x, y):
        return sign(x - q_x), sign(y - q_y)

    if which_square(k_x, k_y) == which_square(dest_x, dest_y):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：n=10
    main(10)