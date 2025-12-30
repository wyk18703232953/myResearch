def main(n: int):
    # 根据 n 生成测试数据：让 l 和 r 在 [0, 2^n - 1] 范围内变化
    # 这里给一个典型构造：l = 0, r = 2^n - 1
    # 可根据需要修改为其他生成方式
    l = 0
    r = (1 << n) - 1

    z = l ^ r
    c = 0
    if z == 0:
        print(0)
        return
    while z:
        c += 1
        z >>= 1
    x = '1' * c
    print(int(x, 2))


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)