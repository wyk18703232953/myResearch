from math import pow

def main(n):
    # 根据规模 n 生成测试数据：这里直接用 n 作为原程序中的输入
    n = int(n) - 1
    x = 1
    y = 9
    while n > x * y:
        n -= x * y
        x += 1
        y *= 10
    a = int(pow(10, x - 1)) + int(n / x)
    z = str(a)
    which = n % x
    print(z[which])