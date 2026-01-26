def main(n: int):
    # 根据 n 生成测试数据 m，这里示例使用一个与 n 相关的数
    # 可以根据需要修改生成规则
    m = 10 ** 6 + n

    if n < 30:
        result = m % (2 ** n)

    else:
        result = m

    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用
    for n in range(1, 35):
        main(n)