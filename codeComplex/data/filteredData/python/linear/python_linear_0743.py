def main(n: int):
    # 根据规模 n 生成测试数据，这里直接使用 n 作为规模参数
    # 若需要复杂测试数据生成逻辑，可在此扩展
    ans = 1
    for i in range(1, n):
        ans += i * 4
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可修改此处的参数
    main(10)