def s(k: int) -> int:
    if k % 2 == 0:
        return k // 2
    else:
        return - (k + 1) // 2


def main(n: int):
    """
    n 为测试数据规模，即生成的区间数量。
    生成 n 组 (l, r) 测试数据，并输出原程序对应的结果。
    测试数据规则：
      第 i 组：l = i, r = 2 * i
    """
    for i in range(1, n + 1):
        l = i
        r = 2 * i
        print(s(r) - s(l - 1))


if __name__ == "__main__":
    # 示例：运行 main(5) 生成 5 组测试并打印结果
    main(5)