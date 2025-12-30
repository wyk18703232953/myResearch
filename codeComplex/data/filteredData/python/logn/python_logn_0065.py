def bina(bi):
    binary1 = bi
    decimal, i, n = 0, 0, 0
    while bi != 0:
        dec = bi % 10
        decimal = decimal + dec * pow(2, i)
        bi = bi // 10
        i += 1
    return decimal

def con(n):
    return bin(n).replace("0b", "")

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里示例为：l = n, r = 2*n + 1
    # 可根据需要调整生成策略
    l = n
    r = 2 * n + 1

    k = con(l)
    m = con(r)
    k = list(str(k))
    m = list(str(m))
    j = len(m) - len(k)
    k = ['0'] * j + k

    c = 0
    for i in range(len(m)):
        if k[i] != m[i]:
            c = 1
        if k[i] == m[i] and k[i] == '1' and c == 1:
            k[i] = '0'
        elif k[i] == m[i] and k[i] == '0' and c == 1:
            k[i] = '1'

    k_int = int(''.join(k))
    m_int = int(''.join(m))
    result = bina(k_int) ^ bina(m_int)
    print(result)
    return result

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)