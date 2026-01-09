def main(n):
    # 映射 n 为输入规模，这里使用线性关系构造 a, b
    # 保证 b 不为 0 且变化随 n 增长
    a = n * n + 3 * n + 7
    b = n + 1

    if a % b == 0:
        # print(int(a / b))
        pass

    else:
        c = 0
        while b:
            c += a // b
            temp = a
            a = b
            b = temp % b
        # print(c)
        pass
if __name__ == "__main__":
    main(10)