def main(n):
    """
    n 作为规模参数，用来生成一组 (l, r) 测试数据并执行原逻辑。
    这里简单设定：
        l = 0
        r = n
    并计算在 [l, r] 区间内能得到的最大 XOR 值。
    """
    l = 0
    r = n

    if l != r:
        binary_r = bin(r)[2:]
        binary_l = bin(l)[2:].zfill(len(binary_r))

        max_idx_prefix = 0
        for idx, l_digit in enumerate(binary_l):
            if l_digit != binary_r[idx]:
                max_idx_prefix = idx
                break

        a_binary = [0 for _ in range(len(binary_r))]
        a_binary[max_idx_prefix] = 0
        for idx in range(max_idx_prefix + 1, len(a_binary)):
            a_binary[idx] = 1

        b_binary = [0 for _ in range(len(binary_r))]
        b_binary[max_idx_prefix] = 1

        a_binary = ''.join(str(digit) for digit in a_binary)
        b_binary = ''.join(str(digit) for digit in b_binary)

        a_binary = int(a_binary, 2)
        b_binary = int(b_binary, 2)

        max_xor = a_binary ^ b_binary

        # print(max_xor)
        pass

    else:
        # print(l ^ r)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)