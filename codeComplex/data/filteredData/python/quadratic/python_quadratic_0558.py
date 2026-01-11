import sys

def main(n):
    # 这里根据 n 生成测试数据：令 m = n
    m = n

    for i in range(1, n // 2 + 1):
        for j in range(1, m + 1):
            # sys.stdout.write(f"{i} {j}\n")
            # sys.stdout.write(f"{n - i + 1} {m - j + 1}\n")
            pass

    if n % 2 == 1:
        mid_row = n // 2 + 1
        for j in range(1, m // 2 + 1):
            # sys.stdout.write(f"{mid_row} {j}\n")
            # sys.stdout.write(f"{mid_row} {m - j + 1}\n")
            pass
        if m % 2 == 1:
            # sys.stdout.write(f"{mid_row} {m // 2 + 1}\n")
            pass


if __name__ == "__main__":
    # 示例：当作脚本运行时，用 n = 5 测试
    main(5)