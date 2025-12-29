import random

def main(n: int):
    # 1. 生成测试数据 (x, w)
    # 随机生成 n 个点，每个点有位置 x 和“半径” w
    # 可根据需要调整数据范围
    X_MAX = 10**6
    W_MAX = 10**3

    V = []
    for _ in range(n):
        x = random.randint(-X_MAX, X_MAX)
        w = random.randint(0, W_MAX)
        V.append((x - w, x + w))

    # 2. 按右端点排序
    V.sort(key=lambda x: x[1])

    # 3. 贪心选择不相交区间数量
    if n == 0:
        print(0)
        return

    ans = 1
    now = V[0]
    for i in range(1, n):
        if V[i][0] >= now[1]:
            now = V[i]
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)