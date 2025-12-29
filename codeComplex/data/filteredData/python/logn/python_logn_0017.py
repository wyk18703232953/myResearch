def main(n: int):
    """
    根据规模 n 生成一组 (l, r)，并输出原程序逻辑的结果。
    这里简单设定：
        l = 0
        r = n
    若需其他测试方式，可在此处调整生成规则。
    """
    l, r = 0, n

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
    # 示例：调用 main(10)
    main(10)