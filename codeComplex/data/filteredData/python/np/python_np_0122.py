import random

def main(n):
    # 生成规模为 n 的测试数据：n 个随机整数
    # 可按需调整随机范围
    xs = [random.randint(0, 10**9) for _ in range(n)]

    m = n
    b = []
    k = []
    for i in range(m):
        x = xs[i]
        c = 0
        for j in range(len(b)):
            v = b[j]
            d = k[j]
            if (x ^ v) < x:
                x ^= v
                c ^= d

        if x != 0:
            print(0)
            c ^= 2 ** i
            b.append(x)
            k.append(c)
        else:
            a = []
            tmp_c = c
            for j in range(m):
                if tmp_c & 1 == 1:
                    a.append(j)
                tmp_c >>= 1
            print(len(a), end='')
            for v in a:
                print(' ', v, sep='', end='')
            print()


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)