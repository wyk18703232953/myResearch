def main(n: int):
    # 根据规模 n 生成测试数据，这里直接使用 n 作为测试规模
    ans = 1
    for i in range(n):
        ans += i * 4
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main，传入一个规模，例如 10
    main(10)