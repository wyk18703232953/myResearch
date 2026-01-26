def main(n):
    # 映射：原程序中有三个输入 n, a, b
    # 这里使用规模参数 n 生成确定性的 (nn, a, b)
    # 让 nn = n，a 和 b 为一些简单的确定性函数
    if n <= 0:
        return

    nn = n

    # 构造 a, b：满足通常 a == 1 或 b == 1 的约束，以便算法有意义
    # 保证在不同 n 下输入可变化但仍确定性
    if n % 2 == 0:
        a = 1
        b = max(1, (n % 5) + 1)

    else:
        b = 1
        a = max(1, (n % 5) + 1)

    # 保证至少一个为 1
    if a != 1 and b != 1:
        a = 1

    def calc(n_val, a_val, b_val):
        if min(a_val, b_val) != 1:
            # print("NO")
            pass
            return
        if a_val == b_val == 1 and n_val in (2, 3):
            # print("NO")
            pass
            return

        # print("YES")
        pass
        ONE, ZERO = ("10" if a_val > 1 else "01")

        edges = n_val - max(a_val, b_val)
        line = "0" + (ZERO, ONE)[edges > 0] * (n_val > 1) + ZERO * (n_val - 2)
        # print(line)
        pass

        for y in range(1, n_val):
            line = ZERO * (y - 1) + (ZERO, ONE)[y <= edges] + "0"
            if y < n_val - 1:
                line += (ZERO, ONE)[y < edges] + ZERO * (n_val - y - 2)
            # print(line)
            pass

    calc(nn, a, b)


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n
    main(5)