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
    """
    n 作为规模参数，用于生成测试数据。
    这里简单生成两个非负整数：
      x = n
      y = 2*n + 3
    然后调用 maxi(x, y) 并打印结果。
    """
    x = n
    y = 2 * n + 3
    print(maxi(x, y))

if __name__ == "__main__":
    # 示例：使用 n = 10 作为测试规模
    main(10)