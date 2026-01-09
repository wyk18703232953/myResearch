def main(n):
    # 生成确定性的测试数据：列表长度为 n
    # 元素模式：i % (n // 2 + 1)，保证有重复和可能的 0
    if n <= 0:
        # print(0)
        pass
        return

    a = [i % (n // 2 + 1) for i in range(n)]

    b = set(a)
    res = len(b)
    if 0 in b:
        res -= 1
    # print(res)
    pass
if __name__ == "__main__":
    main(10)