def main(n: int):
    # 根据规模 n 生成测试数据：
    # 在 [0, 2^n - 1] 范围内构造一对 l, r，使得 l < r。
    # 这里简单取 l = 0, r = 2^n - 1，覆盖最大的区间。
    if n <= 0:
        # 无有效二进制位时，直接返回
        return

    l = 0
    r = (1 << n) - 1

    # 以下为原逻辑的封装
    if l == r:
        # print(0)
        pass
        return

    binr, binl = list(bin(r)[2:]), list(bin(l)[2:])
    binl = ['0'] * (len(binr) - len(binl)) + binl

    for i in range(len(binl)):
        if binl[i] != binr[i]:
            del binl[0:i]
            del binr[0:i]
            break

    x = '1' * len(binl)
    result = int(x, 2)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改 n 的值
    main(5)