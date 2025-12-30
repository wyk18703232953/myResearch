import random

def main(n: int):
    # 生成测试数据：让 r 的二进制长度约为 n，比特数在 [1, n] 内随机
    if n <= 0:
        n = 1
    bit_len = random.randint(1, n)
    # 保证最高位为 1
    r = random.randint(1 << (bit_len - 1), (1 << bit_len) - 1)
    l = random.randint(0, r)

    ls = str(bin(l))[2:]
    rs = str(bin(r))[2:]
    llog = len(ls)
    rlog = len(rs)
    ans = 0

    if llog < rlog:
        z = rlog - 1
        while z > -1:
            ans += 2 ** z
            z -= 1
    else:
        ct = 0
        stringa = ""
        for i in range(len(ls)):
            if ls[i] == rs[i] and ct == 0:
                stringa += ls[i]
            if ls[i] == "0" and rs[i] == "1":
                ct += 1
                stringa += ls[i]
            if ls[i] == "1" and rs[i] == "0":
                stringa += ls[i]
            if ls[i] == rs[i] and ct > 0:
                stringa += str((int(rs[i]) + 1) % 2)
        ans = (int(stringa, 2) ^ r)

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)