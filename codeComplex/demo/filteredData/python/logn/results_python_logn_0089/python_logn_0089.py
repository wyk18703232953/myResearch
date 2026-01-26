def dec_to_bin(N):
    res = [0] * 64
    pos = 0
    while N != 0:
        last_bit = N & 1
        res[pos] = last_bit
        pos += 1
        N = N >> 1
    return res

def max_xor(a, b):
    a_bin = dec_to_bin(a)
    b_bin = dec_to_bin(b)

    res = ""
    x = ""
    y = ""
    diff_pt_found = False

    for i in range(len(a_bin) - 1, -1, -1):
        if diff_pt_found == False and a_bin[i] == b_bin[i]:
            x += str(a_bin[i])
            y += str(b_bin[i])

        if diff_pt_found == False and a_bin[i] != b_bin[i]:
            diff_pt_found = True
            x += str(a_bin[i])
            y += str(b_bin[i])
            res += "1"
            continue

        if diff_pt_found == True:
            if a_bin[i] != b_bin[i]:
                res += "1"
                x += str(a_bin[i])
                y += str(b_bin[i])
            elif b_bin[i] == 1:
                res += "1"
                x += str(a_bin[i])
                y += str(0)
            elif a_bin[i] == 0:
                res += "1"
                x += str(1)
                y += str(b_bin[i])

    return x, y, res

def bin_to_dec(bstr):
    bstr = str(bstr)
    mul = 1
    res = 0
    for i in range(len(bstr) - 1, -1, -1):
        if bstr[i] == '1':
            res += mul
        mul = mul * 2
    return res

def main(n):
    # 确定性生成 a, b，二者都是随 n 规模线性增长的整数
    # 保证不同 n 有不同规模的位数，以便做时间复杂度实验
    # 这里生成两个在 [0, 2^n) 范围内的数（当 n > 60 时受 64 位限制，但逻辑保持不变）
    if n <= 0:
        a = 0
        b = 0

    else:
        max_bits = 60  # 与 dec_to_bin 的 64 位上限一致，避免无意义大数
        bits = n if n < max_bits else max_bits
        # 构造具有一定模式的位串：奇偶位交错
        a = 0
        b = 0
        for i in range(bits):
            if i % 2 == 0:
                a |= (1 << i)

            else:
                b |= (1 << i)
        # 再加入与 n 相关的偏移，让不同 n 时数值不同
        a ^= (n << (bits // 2))
        b ^= (n * 3 << (bits // 3 if bits // 3 > 0 else 0))

    x, y, res = max_xor(a, b)
    # print(bin_to_dec(res))
    pass
if __name__ == "__main__":
    main(20)