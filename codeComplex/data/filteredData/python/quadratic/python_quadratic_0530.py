def main(n: int) -> int:
    # 这里将原来的 input() 改为由参数 n 提供规模
    i = int(n)
    v = 0
    g = 2
    s = 4
    while g <= i:
        while s <= i:
            v = v + int(s / g * 4)
            s = s + g
        g = g + 1
        s = g * 2
    return v


if __name__ == "__main__":
    # 根据 n 生成测试数据：这里直接选取几个典型规模进行调用演示
    # 实际使用时，可根据需要替换或扩展这些规模
    for n in [1, 2, 5, 10, 20]:
        print(f"n = {n}, v = {main(n)}")