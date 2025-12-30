class Read:
    @staticmethod
    def calc(sep=0, k=0):
        count = 0
        for i in range(sep):
            j = sep - i
            s = ((i + 1) * i) / 2
            if (s - j == k):
                return j
        return count


def main(n):
    """
    n: 问题规模，用来生成测试数据 (n, k)
       这里示例生成 k = n // 2，实际可按需要调整生成方式
    """
    # 根据 n 生成测试数据 (n, k)
    k = n // 2

    # 调用原逻辑
    result = Read.calc(n, k)

    # 输出结果
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)