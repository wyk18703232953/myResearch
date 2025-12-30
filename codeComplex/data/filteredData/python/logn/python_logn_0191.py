import random

def digit_sum(x: int) -> int:
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def main(n: int):
    # 生成测试数据：随机生成 k，范围 [1, n]（也可按需要调整）
    if n <= 0:
        print(0)
        return

    k = random.randint(1, n)

    x, y = 1, n
    f = 0
    m = 0  # 保证作用域内存在 m
    while x <= y:
        m = (x + y) // 2
        s = digit_sum(m)
        m1 = m - 1
        s1 = digit_sum(m1) if m1 > 0 else 0

        if m == 0 or (m - s >= k and m1 - s1 < k):
            f = 1
            break
        elif m - s < k:
            x = m + 1
        else:
            y = m - 1

    if f:
        print(n - m + 1)
    else:
        print(0)


if __name__ == "__main__":
    # 示例运行：可修改 n 测试不同规模
    main(10**6)