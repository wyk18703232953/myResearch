import random

def main(n):
    # 生成测试数据
    # t 取 [0, 10] 范围内的整数
    t = random.randint(0, 10)
    segments = []
    for _ in range(n):
        # x 在 [-100, 100] 内，a 为正数 [1, 20]
        x = random.randint(-100, 100)
        a = random.randint(1, 20)
        segments.append((x, a))

    # 原始逻辑开始
    lst = []
    for x, a in segments:
        lst.append((x - a / 2, x + a / 2))

    lst.sort()
    if n == 0:
        ans = 0
    else:
        ans = 2
        for i in range(n - 1):
            dis = lst[i + 1][0] - lst[i][1]
            if dis > t:
                ans += 2
            elif dis == t:
                ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)