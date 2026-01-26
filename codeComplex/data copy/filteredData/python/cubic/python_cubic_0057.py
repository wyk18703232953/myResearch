def main(n):
    # 根据 n 生成测试数据，这里生成一个长度为 n 的字符串：
    # 前半部分为 'a'，后半部分为 'b'，保证有一定的重复结构。
    # 你可以根据需要改成其他生成方式。
    half = n // 2
    a = "a" * half + "b" * (n - half)

    n = len(a)
    for l in range(n, 0, -1):
        for i in range(n - l + 1):
            if a[i:i + l] in a[i + 1:]:
                # print(l)
                pass
                return
    # print(0)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)