import os
import random

def main(n):
    # 根据 n 生成测试数据：n 个随机 0..(2^31-1) 的整数
    # 可根据需要调整生成方式
    random.seed(0)
    numbs = [random.getrandbits(31) for _ in range(n)]

    base = []
    out = []

    for i in range(n):
        x = numbs[i]
        how = 0

        for b, rep in base:
            if x.bit_length() == b.bit_length():
                x ^= b
                how ^= rep

        if x:
            how |= 1 << i

            a = 0
            b_len = len(base)
            while a < b_len:
                c = (a + b_len) >> 1
                if base[c][0] > x:
                    a = c + 1
                else:
                    b_len = c
            base.insert(a, (x, how))

            out.append(0)
        else:
            outind = len(out)
            out.append(-1)

            y = bin(how).encode('ascii')
            ylen = len(y)
            for j in range(2, len(y)):
                if y[j] == 49:  # ord('1') == 49
                    out.append(ylen - 1 - j)
            out[outind] = len(out) - 1 - outind

    os.write(1, b'\n'.join(str(x).encode('ascii') for x in out))


# 示例：需要时可以手动调用 main(n)
# if __name__ == "__main__":
#     main(10)