def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里简单地令 a 和 b 为两个 n 位以内的正整数
    # 例如：a = 2^n - 2, b = 2^n - 1（保证 a != b 且二进制长度大致为 n）
    if n <= 1:
        # 对于非常小的 n，给一个固定例子
        a, b = 1, 2
    else:
        a = (1 << n) - 2
        b = (1 << n) - 1

    if a == b:
        print(0)
        return

    aa = ""
    bb = ""
    ta, tb = a, b  # 保留原始值如果需要调试

    while ta or tb:
        aa += str(ta % 2)
        bb += str(tb % 2)
        ta //= 2
        tb //= 2

    aa = aa[::-1]
    bb = bb[::-1]

    idx = 0
    # 为避免索引越界，对较短的补齐前导 0
    if len(aa) < len(bb):
        aa = aa.zfill(len(bb))
    elif len(bb) < len(aa):
        bb = bb.zfill(len(aa))

    while idx < len(aa) and aa[idx] == bb[idx]:
        idx += 1

    ln = len(aa)
    r = 2 ** (ln - idx) - 1
    print(r)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)