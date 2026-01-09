def main(n: int):
    # 生成测试数据：根据题意原本是从输入中读取 (n, k)
    # 这里我们用 n 作为规模，并构造一个与 n 同尺度的 k，例如 k = n
    k = n if n > 0 else 1  # 避免除零

    a, b, c = 2 * n, 5 * n, 8 * n
    ceil = lambda x, y: (x + y - 1) // y
    result = ceil(a, k) + ceil(b, k) + ceil(c, k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模自行设定
    main(10)