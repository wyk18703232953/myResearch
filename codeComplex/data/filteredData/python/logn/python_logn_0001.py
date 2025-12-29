import random


def field(n, x, y, t):
    t = t + 1
    upper_dist = x - 1
    left_dist = y - 1
    down_dist = n - x
    right_dist = n - y
    out_up = max(0, t - upper_dist - 1)
    out_down = max(0, t - down_dist - 1)
    out_left = max(0, t - left_dist - 1)
    out_right = max(0, t - right_dist - 1)
    return (
        base_field(t)
        - right_field(out_right)
        - right_field(out_left)
        - up_field(out_up, n, y)
        - up_field(out_down, n, y)
    )


def right_field(out_r):
    return out_r ** 2


def up_field(out_up, n, y):
    rect = max(0, out_up - n + 1)
    h = out_up - rect
    wyst = max(y - 1 + h - n, 0, h - y)
    result = n * rect + h ** 2 - int((1 + wyst) / 2 * wyst)
    if result < 0:
        result = 0
    return result


def base_field(t):
    return 2 * (t ** 2) - 2 * t + 1


def solve_single(n, x, y, c):
    search = 0
    mid = 1
    found = False
    last_sm = 0
    while not found:
        ff = field(n, x, y, search)
        if ff == c:
            found = True
        elif ff > c:
            if search - last_sm == 1:
                found = True
            else:
                search = last_sm + (search - last_sm) // 2
        else:
            last_sm = search
            search += mid
            mid = search - last_sm
    return search


def main(n):
    # 生成测试数据：
    # 棋盘大小 n，随机选择 (x, y)，随机选择 t，然后计算对应的 c = field(...)
    x = random.randint(1, n)
    y = random.randint(1, n)
    # t 的范围随 n 调整，这里简单取 [0, 2*n] 范围内的某个值
    true_t = random.randint(0, 2 * n)
    c = field(n, x, y, true_t)

    ans = solve_single(n, x, y, c)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，给定规模 n
    main(10)