def main(n):
    import math
    # 确定性生成输入：将 n 映射为一对整数 (l, r)
    # 这里设定一个可扩展的映射方式：
    # l = n
    # r = n ^ (n // 2)
    l = n
    r = n ^ (n // 2)

    l_xor_r = l ^ r
    if l_xor_r:
        k = int(math.log(l_xor_r, 2))
        result = (1 << (k + 1)) - 1
        # print(result)
        pass

    else:
        # print(0)
        pass
if __name__ == "__main__":
    main(10)