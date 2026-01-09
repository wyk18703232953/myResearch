def main(n: int):
    # 根据规模 n 生成测试数据，这里假设就是单个整数 n 本身
    # 如需更复杂的生成方式，可在此处修改
    res = []
    multiplier = 1
    cur_n = n

    while cur_n > 1:
        new_n = cur_n // 2
        res.extend((multiplier,) * (cur_n - new_n))
        if cur_n == 3:
            multiplier *= 3

        else:
            multiplier *= 2
        cur_n = new_n

    res.extend((multiplier,) * cur_n)
    # print(*res)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)