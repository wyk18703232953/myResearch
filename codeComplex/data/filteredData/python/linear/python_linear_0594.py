def main(n: int):
    # 根据 n 生成测试数据，这里原逻辑只与单个 n 有关，
    # 所以直接使用传入的 n 作为测试规模参数。
    r = 0
    i = 2
    while i * 2 <= n:
        a = n // i
        r += (a + 2) * (a - 2 + 1) / 2
        i += 1
    print(int(4 * r))


if __name__ == "__main__":
    # 示例：可以在这里调用 main 并传入任意 n 作为规模
    # 比如测试 n = 100
    main(100)