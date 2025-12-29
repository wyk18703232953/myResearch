from random import randint, choice

def main(n):
    # 生成规模为 n 的测试数据（牌面字符串列表）
    # 每张牌形式如 "1m", "9p", "5s"，花色从 m/p/s 中随机选
    suits = ['m', 'p', 's']
    t = [str(randint(1, 9)) + choice(suits) for _ in range(n)]

    # 原逻辑开始
    t = t[:3]  # 原程序只取前 3 张牌参与计算
    s_set = set(t)
    res = 3
    if len(s_set) == 1:
        res = min(res, 0)
    elif len(s_set) == 2:
        res = min(res, 1)
    elif len(s_set) == 3:
        res = min(res, 2)
    if res == 0:
        print(res)
        return

    t.sort()
    m = [int(a[0]) for a in t if a[1] == 'm']
    p = [int(a[0]) for a in t if a[1] == 'p']
    s = [int(a[0]) for a in t if a[1] == 's']

    def f(a):
        res_local = 2
        for i in a:
            if ((i - 1 in a and i + 1 in a) or
                (i - 2 in a and i - 1 in a) or
                (i + 1 in a and i + 2 in a)):
                return 0
            elif (i - 1 in a or i + 1 in a or
                  i - 2 in a or i + 2 in a):
                res_local = min(res_local, 1)
        return res_local

    res = min([res, f(m), f(p), f(s)])
    print(res)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)