def main(n):
    # 映射：n -> n 行，m 列，其中 m = max(1, n)
    m = max(1, n)

    # 构造一个 n x m 的确定性整型矩阵 a
    # a[i][j] = (i + 1) * (j + 2)
    a = [[(i + 1) * (j + 2) for j in range(m)] for i in range(n)]

    # 如果 n 为 0，则没有行可检查，直接输出 "NO"
    if n == 0:
        # print("NO")
        pass
        return

    # 计算列和
    colsums = [sum(a[i][j] for i in range(n)) for j in range(m)]

    # 保留原有逻辑：若存在一行，满足所有元素严格小于对应列和，则输出 "YES"
    for row in a:
        if all(rv < sv for (rv, sv) in zip(row, colsums)):
            # print("YES")
            pass
            return

    # print("NO")
    pass
if __name__ == "__main__":
    # 示例：使用 n = 5 作为规模参数
    main(5)