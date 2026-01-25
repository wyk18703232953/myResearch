def main(n):
    # 解释规模含义：
    # n: 原问题中的 n
    # m: 与 n 同规模，设为 n
    # 接下来生成 m 组 (x, d)，完全确定性
    m = n

    a = (n * (n - 1)) // 2
    n2 = n // 2
    b = n2 * (n2 + 1)
    if n % 2 == 0:
        b -= n2

    s = 0
    for i in range(m):
        # 确定性构造 x, d
        x = i  # 0,1,2,...,m-1
        # 构造 d 为负、零、正交替出现，且随 i 增长
        if i % 3 == 0:
            d = i  # 非负
        elif i % 3 == 1:
            d = -i  # 非正
        else:
            d = 0
        s += x * n
        s += d * (a if d > 0 else b)

    return s / n


if __name__ == "__main__":
    # 示例调用
    result = main(10)
    print(result)