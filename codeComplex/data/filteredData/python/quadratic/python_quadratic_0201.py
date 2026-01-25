n, m = 0, 0

def generate_input(n_scale):
    # 设定行数为 n_scale，列数为 n_scale+1，保证 m >= 1
    n = max(1, n_scale)
    m = n + 1
    a = []
    for i in range(n):
        # 生成一个确定性的二进制串，长度为 m
        # 第 i 行第 j 位为 ((i + j) % 2)
        bits = ''.join('1' if (i + j) % 2 == 0 else '0' for j in range(m))
        a.append(int(bits, 2))
    return n, m, a

def main(n_scale):
    global n, m
    n, m, a = generate_input(n_scale)

    s = 0
    t = 0
    for x in a:
        t |= s & x
        s |= x
    print(('YES', 'NO')[all(x & s & ~t for x in a)])

if __name__ == "__main__":
    main(5)