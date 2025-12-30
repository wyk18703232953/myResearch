import random

def main(n: int):
    # 随机生成 m（列数），范围可根据需要调整
    m = max(1, n // 2)

    # 生成测试数据：n 行，每行是一个长度为 m 的 0-9 随机整数列表
    a = [
        [random.randint(0, 9) for _ in range(m)]
        for _ in range(n)
    ]

    # 计算每一列的列和
    colsums = [sum(a[i][j] for i in range(n)) for j in range(m)]

    # 检查是否存在一行，其每个元素都严格小于对应列和
    for row in a:
        if all(rv < sv for (rv, sv) in zip(row, colsums)):
            print("YES")
            return

    print("NO")


if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(5)