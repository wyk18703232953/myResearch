def main(n: int):
    # 根据 n 生成测试数据，这里直接使用参数 n 作为规模
    summ = 1
    for i in range(1, n):
        summ += i * 4
    # print(summ)
    pass
if __name__ == "__main__":
    # 示例：可自行修改测试规模
    main(10)