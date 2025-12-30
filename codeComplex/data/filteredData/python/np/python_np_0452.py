from math import gcd

def main(n):
    # 这里的 n 既作为规模，又作为原程序里的第一个输入参数 n 使用
    # 自动生成 x, y，使得与 n 之间有一定变化关系，且 gcd(x, y) 不为 0
    # 你可以根据需要修改生成规则
    x = n * 2 + 1
    y = n * 3 + 2

    g = gcd(x, y)
    n2 = n // g
    x2 = x // g
    y2 = (x + y) // g
    r = n % g

    def f(val, s):
        d0 = -val
        d1 = -val
        if s == 0:
            d0 = 0
        else:
            d1 = 0
        for i in range(y2):
            t0 = max(d0, d1)
            t1 = d0 + val // y2 + (1 if (i * x2) % y2 < val % y2 else 0)
            d0, d1 = t0, t1
        return d0 if s == 0 else d1

    def h(v):
        return max(f(v, 0), f(v, 1))

    result = h(n2 + 1) * r + h(n2) * (g - r)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)