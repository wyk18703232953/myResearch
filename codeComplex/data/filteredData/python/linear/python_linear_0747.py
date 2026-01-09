def main(n: int):
    # 根据 n 生成测试数据（本题 n 即为规模，直接使用给定 n）
    # 如果需要基于规模自动生成 n，例如取 n = 10，可改为：n = 10
    ans = 1
    for i in range(n):
        ans += 4 * i
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：自行指定规模 n
    main(10)