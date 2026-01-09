def bin_custom(a):
    if a <= 1:
        return a

    else:
        return 10 * bin_custom(a // 2) + a % 2

def convBin(a):
    k, i = 0, 0
    while a != 0:
        k += (a % 10) * int((2 ** i))
        a //= 10
        i += 1
    return k

def maxi(a, b):
    if a == b:
        return 0
    elif a + 1 == b:
        return a ^ b
    elif a + 2 == b:
        x = a ^ (a + 1)
        y = a ^ (a + 2)
        z = (a + 1) ^ (a + 2)
        return max(max(x, y), z)

    else:
        x = str(bin_custom(a ^ b))
        y = '1' * len(x)
        return convBin(int(y))

def main(n):
    # 根据规模 n 生成测试数据
    # 这里用 n 和 2*n 作为一组测试数据
    a0 = n
    a1 = 2 * n
    result = maxi(a0, a1)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)