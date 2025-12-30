import random

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
        if diff_pt_found is False and a_bin[i] == b_bin[i]:
            x += str(a_bin[i])
            y += str(b_bin[i])

        if diff_pt_found is False and a_bin[i] != b_bin[i]:
            diff_pt_found = True
            x += str(a_bin[i])
            y += str(b_bin[i])
            res += "1"
            continue

        if diff_pt_found is True:
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

def bin_to_dec(bin_val):
    bin_val = str(bin_val)
    mul = 1
    res = 0
    for i in range(len(bin_val) - 1, -1, -1):
        if bin_val[i] == '1':
            res += mul
        mul = mul * 2
    return res

def main(n):
    # 根据规模 n 生成测试数据，这里使用 n 作为上界生成两个随机整数 a, b
    if n <= 0:
        n = 1
    a = random.randint(0, n)
    b = random.randint(0, n)

    x, y, res = max_xor(a, b)
    print(bin_to_dec(res))

if __name__ == "__main__":
    # 示例：以 100 作为规模调用 main
    main(100)