import random

def main(n):
    # 生成测试数据
    # capacity 与数据规模相关，这里设为 n * 100 的量级
    capacity = random.randint(n * 50, n * 150)
    a = []

    # 生成 n 个 (x, y)，保证非负且有一定大小
    for _ in range(n):
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        a.append((x, y))

    # 原逻辑开始
    a.sort(key=lambda x: max(0, x[0] - x[1]))

    current_sum = 0
    i = n - 1
    ans = 0
    for x in a:
        current_sum += x[0]

    while i >= 0 and current_sum > capacity:
        ans += 1
        current_sum -= max(0, a[i][0] - a[i][1])
        i -= 1

    if current_sum <= capacity:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)