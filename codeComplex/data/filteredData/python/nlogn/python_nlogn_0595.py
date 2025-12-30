import random

def main(n: int):
    # 生成测试数据：
    # n 为数组长度，m 为未使用参数，保留结构一致性
    m = random.randint(1, max(1, n * 2))
    # 生成 n 个 1..m 的随机整数
    a = [random.randint(1, m) for _ in range(n)]

    # 原逻辑
    a.sort()
    h = 0
    ans = 0
    for i in range(n - 1):
        ans += a[i] - 1
        if a[i] > h:
            h += 1
    if h < max(a):
        ans += h
    else:
        ans += a[-1] - 1
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)