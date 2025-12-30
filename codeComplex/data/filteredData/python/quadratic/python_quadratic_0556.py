def main(n):
    # 生成测试数据：给定规模 n，构造 m，并在函数内完成计算与输出
    # 这里选择 m = n，若需要其他关系，可自行修改
    m = n

    if m % 2 == 0:
        steps = []
        for j in range(m // 2):
            for i in range(n):
                steps.append((j, i))
                steps.append((m - j - 1, n - i - 1))
    else:
        steps = []
        for j in range(m // 2):
            for i in range(n):
                steps.append((j, i))
                steps.append((m - j - 1, n - i - 1))
        l = 0
        r = n - 1
        mid = m // 2
        while l <= r:
            steps.append((mid, l))
            if l != r:
                steps.append((mid, r))
            l += 1
            r -= 1

    for x, y in steps:
        print(y + 1, x + 1)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)