from math import log

def func(n, i):
    if n == 3:
        return (str(1 * i) + ' ') + (str(1 * i) + ' ') + (str(3 * i))
    if n % 2 == 0:
        odd = n // 2

    else:
        odd = n // 2 + 1
    q = 1 * i
    s = (str(q) + ' ') * odd
    return s

def main(n: int):
    # 使用 n 作为规模生成测试数据，这里直接用 n 作为原程序中的输入
    if n == 3:
        s = '1 1 3'

    else:
        s = ''
        z = 1
        while n > 0:
            s = s + func(n, z)
            z = z * 2
            if n == 3:
                break
            if n % 2 == 0:
                odd = n // 2

            else:
                odd = n // 2 + 1
            n = n - odd
    # print(s)
    pass

# 示例：调用 main(10)
if __name__ == "__main__":
    main(10)