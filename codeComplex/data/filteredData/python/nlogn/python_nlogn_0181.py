import random

def main(n: int):
    # 生成规模为 n 的测试数据：(x, w) 对
    # 可根据需要调整数据范围
    xs = [random.randint(-10**9, 10**9) for _ in range(n)]
    ws = [random.randint(0, 10**9) for _ in range(n)]
    rng = [(x - w, x + w) for x, w in zip(xs, ws)]

    # 按右端点升序排序，右端点相同时按左端点升序
    rng.sort(key=lambda x: (x[1], x[0]))

    ans = 0
    tmp = -10**10
    for l, r in rng:
        if tmp <= l:
            ans += 1
            tmp = r

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)