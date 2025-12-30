import os
import random


def solve(arr):
    n = len(arr)
    numbs = [n] + arr[:]  # 模拟原来从 stdin 读入的 numbs，首元素是 n

    n = numbs.pop(0)

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

    return out


def main(n: int):
    # 根据 n 生成测试数据：生成 n 个随机 64 位非负整数
    random.seed(0)
    arr = [random.getrandbits(64) for _ in range(n)]

    result = solve(arr)
    os.write(1, b'\n'.join(str(x).encode('ascii') for x in result))


if __name__ == "__main__":
    # 示例：可在此处修改 n 以测试
    main(10)