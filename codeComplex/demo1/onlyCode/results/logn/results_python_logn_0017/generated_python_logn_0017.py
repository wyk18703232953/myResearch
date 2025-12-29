def main(n: int):
    """
    将原程序改为可参数化规模 n 的版本。
    这里根据 n 生成一组 (l, r) 测试数据：
      - l = 0
      - r = (1 << n) - 1  （即 n 位全为 1 的二进制数）
    可根据需要自行修改生成策略。
    """
    # 生成测试数据
    l = 0
    r = (1 << n) - 1  # 保证 r >= l，且规模由 n 控制

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
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)