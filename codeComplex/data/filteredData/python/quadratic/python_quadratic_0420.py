def main(n: int):
    # 生成长度为 n 的测试字符串 t（周期性模式，便于验证）
    base = "abc"
    t = (base * ((n + len(base) - 1) // len(base)))[:n]

    # 可根据需要调整 k 的规模，这里设为 3 作为示例
    k = 3

    i = 1
    while t[:-i] != t[i:]:
        i += 1
    # print(t[:i] * k + t[i:])
    pass
if __name__ == "__main__":
    # 示例：当作脚本运行时，给一个默认 n 测试
    main(10)