def main(n):
    # n 作为输入规模，同时生成 n 和 m，令 m == n 保持规模一致
    m = n
    # 生成长度为 m 的输入列表 l，元素在 1..n 范围内，使用简单确定性映射
    if n <= 0:
        # print(0)
        pass
        return

    l = [(i % n) + 1 for i in range(m)]

    square = [0] * n
    for x in l:
        square[x - 1] += 1
    # print(min(square))
    pass
if __name__ == "__main__":
    main(10)