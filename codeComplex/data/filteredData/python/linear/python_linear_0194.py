import random

def main(n):
    # 生成测试数据
    # 约束可以根据需要调整
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    T = random.randint(1, 100)

    ts = [random.randint(0, T) for _ in range(n)]
    ts.sort()

    ans = 0
    for t in ts:
        temp = -10**18
        for u in range(t, T + 1):
            temp = max(temp, c * (u - t) + a - b * (u - t))
        ans += temp

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)