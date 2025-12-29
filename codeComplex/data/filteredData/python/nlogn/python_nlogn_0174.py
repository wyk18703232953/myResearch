import random

def main(n: int):
    # 生成测试数据：n 个 (x, w) 对
    # 可根据需要调整数据范围
    xw = []
    for _ in range(n):
        x = random.randint(-10**6, 10**6)
        w = random.randint(0, 10**6)
        xw.append([x, w])

    # 原逻辑开始
    ab = sorted([[x - w, x + w] for x, w in xw], key=lambda x: (x[1], x[0]))

    if not ab:
        print(0)
        return

    k = ab[0][0]
    cnt = 0
    for a, b in ab:
        if k <= a:
            cnt += 1
            k = b

    print(cnt)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)