def main(n: int):
    """
    规模 n 用来生成一组 [l, r] 测试数据。
    这里简单设定：
      l = 0
      r = (1 << n) - 1   # 即 2^n - 1
    你可以按需修改生成方式。
    """
    # 生成测试数据
    l = 0
    r = (1 << n) - 1

    # 原 solve 逻辑
    if l == r:
        print(0)
        return
    mx = str(bin(l ^ r))
    x = len(mx[2:])
    print(2 ** x - 1)


if __name__ == "__main__":
    # 示例: 规模为 5
    main(5)