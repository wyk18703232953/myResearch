def main(n):
    # 生成测试数据，这里根据规模 n 构造 k
    # 可根据需要调整生成规则
    k = n + 1 if n > 0 else 1

    result = ((8 * n + k - 1) // k +
              (5 * n + k - 1) // k +
              (2 * n + k - 1) // k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可以修改这里的 n 进行测试
    main(10)