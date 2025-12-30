def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里约定：生成一对整数 (l, r)，其中
    # l = 0
    # r = (1 << n) - 1  （即 n 位全为 1 的数）
    # 你也可以按需要自定义生成逻辑
    if n <= 0:
        l, r = 0, 0
    else:
        l, r = 0, (1 << n) - 1

    # 原逻辑
    if l == r:
        ans = 0
    else:
        ans = 2 ** len(bin(l ^ r)[2:]) - 1

    print(ans)


if __name__ == "__main__":
    # 示例：用 n = 5 运行
    main(5)