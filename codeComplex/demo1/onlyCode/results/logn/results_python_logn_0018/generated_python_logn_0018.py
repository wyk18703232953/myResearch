def main(n: int):
    """
    规模 n 用于生成 (l, r) 测试数据：
    这里约定：
      - l = 0
      - r = (1 << n) - 1   （即 n 位全为 1）
    你可以按需要修改生成方式。
    """
    # 1. 生成测试数据（可按需求替换）
    l = 0
    r = (1 << n) - 1

    # 2. 原逻辑
    if l == r:
        print(0)
        return

    binr, binl = bin(r)[2:], bin(l)[2:]
    binl = '0' * (len(binr) - len(binl)) + binl

    for i in range(len(binl)):
        if binl[i] != binr[i]:
            binl = '1' * len(binl[i:])
            break

    print(int(binl, 2))


if __name__ == "__main__":
    # 示例：n = 5
    main(5)