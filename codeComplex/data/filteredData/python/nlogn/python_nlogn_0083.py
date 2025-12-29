import random

def main(n):
    # 随机生成 k，1 <= k <= n
    k = random.randint(1, n)

    # 生成测试数据：l 为 n 行 [score, x1, x2, ...] 形式
    # 为了可重复性，也可以固定种子：random.seed(0)
    l = []
    for _ in range(n):
        # score 范围 1~10，后面再加两列随机数据模拟原程序的多列输入
        row = [random.randint(1, 10), random.randint(1, 100), random.randint(1, 100)]
        l.append(row)

    # 原逻辑开始
    l.sort(reverse=True)
    c = 0
    a = l[k - 1][0]
    x, y = k - 1, k - 1

    for i in range(k - 2, -1, -1):
        if l[i][0] == a:
            x = i
        else:
            break

    for i in range(k, n):
        if l[i][0] == a:
            y = i
        else:
            break

    d = k - 1 - x
    d = y - d

    for i in range(y, x - 1, -1):
        if l[i] == l[d]:
            c += 1

    print(c)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)