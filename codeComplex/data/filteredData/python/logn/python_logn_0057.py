def main(n):
    from math import log

    # 确定性生成输入：两个整数 l, r
    l = 1
    r = l + max(1, n)

    # 原始算法逻辑
    i = msb = int(max(log(l, 2), log(r, 2)))
    while ((2 ** i) & l) == ((2 ** i) & r):
        i -= 1
        if i == -1:
            break
    i += 1
    result = 2 ** i - 1

    # print(result)
    pass
if __name__ == "__main__":
    main(10)