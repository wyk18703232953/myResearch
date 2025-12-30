import random

def main(n: int):
    # 生成测试数据：n 个区间的 (x, w)
    # 控制范围避免溢出
    X_MIN, X_MAX = -10**8, 10**8
    W_MIN, W_MAX = 0, 10**8

    li = []
    for _ in range(n):
        x = random.randint(X_MIN, X_MAX)
        w = random.randint(W_MIN, W_MAX)
        # 构造区间 (x-w, x+w)
        li.append((x - w, x + w))

    # 按区间右端点排序
    li.sort(key=lambda x: x[1])

    a = -10 ** 9
    ans = 0

    # 区间调度贪心
    for i in range(n):
        if a <= li[i][0]:
            ans += 1
            a = li[i][1]

    print(ans)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)