import random

def main(n):
    # 生成测试数据：
    # n 支队伍数
    # 随机生成 1 <= k <= n
    # 每支队伍生成两个非负整数成绩 (a, b)，范围可自行调节
    k = random.randint(1, n)
    teams = []
    for _ in range(n):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        teams.append([a, b])

    # 按原逻辑处理
    teams.sort(key=lambda x: x[0] * 100 - x[1], reverse=True)

    kth = teams[k - 1][0] * 100 + teams[k - 1][1]
    count = 0
    for t in teams:
        if t[0] * 100 + t[1] == kth:
            count += 1

    print(count)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行指定
    main(10)