import random

def main(n):
    # n: total number of points (taxis + passengers)
    # 随机生成 m（出租车数量），保证 1 <= m < n
    m = random.randint(1, n - 1)

    # 随机生成不重复的位置并排序
    xs = sorted(random.sample(range(1, 10 * n + 1), n))

    # 随机生成类型：1 表示出租车，0 表示乘客，且数量分别为 m 和 n-m
    ts = [1] * m + [0] * (n - m)
    random.shuffle(ts)

    # 原逻辑开始
    taxi_idx = sorted([xs[idx] for idx in range(n) if ts[idx] == 1])
    passenger_idx = sorted([xs[idx] for idx in range(n) if ts[idx] == 0])

    a_is = [0] * len(taxi_idx)
    t_idx = 0
    p_idx = 0

    while True:
        if p_idx >= len(passenger_idx):
            break

        if t_idx == len(taxi_idx) - 1:
            a_is[t_idx] += 1
        else:
            while t_idx < len(taxi_idx) - 1:
                d1 = abs(passenger_idx[p_idx] - taxi_idx[t_idx])
                d2 = abs(passenger_idx[p_idx] - taxi_idx[t_idx + 1])
                if d1 > d2:
                    t_idx += 1
                else:
                    break

            a_is[t_idx] += 1

        p_idx += 1

    print(' '.join(str(x) for x in a_is))


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)