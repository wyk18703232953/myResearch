def main(n):
    # 根据 n 生成测试数据，这里直接使用传入的 n 作为测试规模
    ans = (2 * (n - 1) ** 2) + 2 * n - 1
    print(ans)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的值进行测试
    main(10)