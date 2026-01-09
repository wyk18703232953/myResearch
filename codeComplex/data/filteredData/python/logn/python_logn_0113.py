def main(n):
    # 根据 n 构造确定性的输入区间 [l, r]
    # 让 r - l 与 n 同阶，且覆盖不同二进制位
    l = n
    r = 2 * n + 1

    ans = 0
    for i in range(61):
        if (l & (1 << i)) ^ (r & (1 << i)):
            ans = (1 << (i + 1)) - 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)