def main(n):
    # 生成确定性的测试数据：长度为 n 的整数数组
    # 元素构造方式：i % (n // 2 + 1)，保证有重复和 0 的出现
    if n <= 0:
        # print(0)
        pass
        return
    a = [i % (n // 2 + 1) for i in range(n)]
    s = set(a)
    s.discard(0)
    # print(len(s))
    pass
if __name__ == "__main__":
    main(10)