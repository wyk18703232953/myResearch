def main(n):
    # 映射规则：给定规模 n，构造一对 (rows, cols)
    # 这里设定：
    #   n <= 0: 不输出
    #   n 为奇数: n 行 n 列
    #   n 为偶数: (n // 2) 行，(n * 2) 列
    if n <= 0:
        return

    if n % 2 == 1:
        rows = n
        cols = n
    else:
        rows = n // 2
        cols = n * 2

    # 保持原算法逻辑不变，只是将 n,m 替换为 rows, cols，并用 print 输出
    total_rows = rows
    total_cols = cols

    for i in range(total_rows // 2 + total_rows % 2):
        x1 = i + 1
        x2 = total_rows - i
        if x1 == x2:
            for j in range(total_cols // 2 + total_cols % 2):
                if j + 1 == total_cols - j:
                    print(f"{x1} {j + 1}")
                else:
                    print(f"{x1} {j + 1}")
                    print(f"{x2} {total_cols - j}")
        else:
            if i % 2 == 0:
                for j in range(total_cols):
                    print(f"{x1} {j + 1}")
                    print(f"{x2} {total_cols - j}")
            else:
                for j in range(total_cols):
                    print(f"{x1} {total_cols - j}")
                    print(f"{x2} {j + 1}")


if __name__ == "__main__":
    # 示例：使用一个固定的规模参数进行调用
    main(10)