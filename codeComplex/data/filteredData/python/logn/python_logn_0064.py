def main(n):
    # 映射：用 n 生成一对 (L, R)，保证 L <= R 且规模随 n 增长
    # 例如：让 R = n 的平方，L = floor(R / 2)
    R = n * n
    L = R // 2

    # 原核心逻辑
    for i in range(64, -1, -1):
        if (L & (1 << i)) != (R & (1 << i)):
            # print((1 << (i + 1)) - 1)
            pass
            return
    # print(0)
    pass
if __name__ == "__main__":
    main(10)