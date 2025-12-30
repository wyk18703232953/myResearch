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
    # 根据规模 n 生成测试数据
    # 这里约定：l = n，r = 2 * n + 1（可按需要调整）
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

    k = int(''.join(k))
    m = int(''.join(m))
    result = bina(k) ^ bina(m)
    print(result)
    return result

# 示例调用
if __name__ == "__main__":
    main(5)