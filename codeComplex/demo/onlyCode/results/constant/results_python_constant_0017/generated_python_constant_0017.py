from math import sqrt
import random


def dist(speed, time, a):
    """
    Distance covered in `time` starting from `speed` with acceleration `a`.
    Does not consider speed limit.
    """
    return speed * time + a * time ** 2 / 2


def travelTime(distance, speed, a, v):
    """
    Time to travel `distance` starting from `speed`,
    with acceleration `a` and max speed `v`.
    """
    t_all = (-speed + sqrt(speed ** 2 + 2 * distance * a)) / a
    t_max = (v - speed) / a

    if t_max >= t_all:
        return t_all
    else:
        return t_max + (distance - dist(speed, t_max, a)) / v


def main(n):
    # 根据规模 n 生成测试数据
    # 尝试让参数随 n 增长，但保持合法约束
    random.seed(0)

    # 基本范围设置
    max_a = max(1, n)          # 加速度上界
    max_v = max(1, 5 * n)      # 最高速度上界
    max_l = max(1, 10 * n)     # 路程上界

    a = random.randint(1, max_a)
    v = random.randint(1, max_v)
    l = random.randint(1, max_l)

    # d 为限制区间起点，保证 0 <= d <= l
    d = random.randint(0, l)

    # w 为限制区间内的最高速度，保持在 [1, v] 内
    w = random.randint(1, max(1, v))

    if v <= w:
        result = travelTime(l, 0, a, v)
    else:
        tw = w / a  # time to gain speed w
        dw = dist(0, tw, a)

        if dw >= d:
            result = travelTime(l, 0, a, v)
        else:
            result = tw + 2 * travelTime((d - dw) / 2, w, a, v) + travelTime(
                l - d, w, a, v
            )

    print(result)


if __name__ == "__main__":
    # 示例：使用 n = 10 调用 main
    main(10)