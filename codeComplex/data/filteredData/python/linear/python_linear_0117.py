def main(n: int):
    # 根据规模 n 生成测试数据（此处 n 即为原程序中的 n）
    a = []
    for i in range(n + 1):
        a.append(((n + 1) - i) * i)
    # print(max(a))
    pass
if __name__ == "__main__":
    # 示例：自行修改 n 以测试不同规模
    main(10)