import random

def main(n: int):
    # 生成测试数据
    # t 取 1~10 之间的整数
    t = random.randint(1, 10)

    # 生成 n 组 (x, a)
    # 为了保证有一定间隔，x 递增，a 为正数
    data = []
    cur_x = 0
    for _ in range(n):
        # 每次 x 增加 0~t 之间的随机值，保证区间有重叠或接近
        cur_x += random.randint(0, t)
        a = random.randint(1, 10)  # 区间宽度相关
        data.append((cur_x, a))

    # 以下是原逻辑
    l = []
    for x, a in data:
        l.append((x - a / 2, x + a / 2))
    l.sort()

    res = 2
    for i in range(n - 1):
        if l[i + 1][0] - l[i][1] == t:
            res += 1
        elif l[i + 1][0] - l[i][1] > t:
            res += 2

    print(res)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)