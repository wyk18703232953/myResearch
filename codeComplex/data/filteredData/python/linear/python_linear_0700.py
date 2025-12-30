def main(n: int):
    """
    将原程序改写为可参数化规模 n 的版本。
    这里根据 n 生成一组 (a, b) 测试数据，然后执行原逻辑。

    测试数据生成策略（可按需要自行修改）：
    - a = n
    - b = n // 2
    """
    a = n
    b = n // 2

    if b >= a - 1:
        print(a - 1)
    else:
        summ = b
        k = a - b
        for i in range(2, k + 1):
            summ += i
        print(summ)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)