def main(n):
    # 将 n 映射为原程序中的 n 和 m（两个数组的长度）
    # 这里选择 n 作为第一个数组长度，2*n 作为第二个数组长度
    length_a = n
    length_b = 2 * n

    # 确定性构造数组 a 和 b
    # a 中为 0 到 length_a-1
    a = [i for i in range(length_a)]
    # b 中为从 n//2 开始的连续整数，制造部分交集
    b = [i for i in range(n // 2, n // 2 + length_b)]

    # 为保持原逻辑，先构造集合加速 "in" 检查，核心输出行为不变
    set_b = set(b)
    output = []
    for i in a:
        if i in set_b:
            output.append(str(i))

    if output:
        # print(" ".join(output))
        pass
if __name__ == "__main__":
    main(10)