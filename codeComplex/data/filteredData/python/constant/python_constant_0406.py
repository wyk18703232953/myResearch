import random

def main(n):
    # 生成测试数据：长度为 n 的整数数组 a 和 b
    # 约束：n 至少为 2 且为偶数，否则无法切片成奇偶两部分
    if n < 2 or n % 2 != 0:
        raise ValueError("n 必须为大于等于 2 的偶数")

    # 生成 a, b，元素范围可自行修改
    a = [random.randint(-10, 10) for _ in range(n)]
    b = [random.randint(-10, 10) for _ in range(n)]

    # 保证 a[::2] 和 a[1::2] 非空（由于 n 为偶数且 >=2，此处必然成立）
    a1 = min(a[::2])
    b1 = max(a[::2])
    c1 = min(a[1::2])
    d1 = max(a[1::2])

    g = sum(b[::2]) / 4
    h = sum(b[1::2]) / 4
    r = abs(b[0] - g) + abs(b[1] - h)

    for i in range(a1, b1 + 1):
        for j in range(c1, d1 + 1):
            if abs(i - g) + abs(j - h) <= r:
                print("YES")
                return
    print("NO")


if __name__ == "__main__":
    # 示例：运行规模 n=6
    main(6)