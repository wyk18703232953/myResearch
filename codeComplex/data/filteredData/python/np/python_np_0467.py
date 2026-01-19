import math

def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    # 将原来的单组输入 (n, x, y) 映射为:
    # n_input = n
    # x = n + 1
    # y = n + 2
    n_input = n
    x = n + 1
    y = n + 2

    g = math.gcd(x, y)
    def h(v):
        return max(f(v, 0, x, y, g), f(v, 1, x, y, g))

    y2 = y + x
    # 按照原程序逻辑计算输出：
    # print(n%g*h(n//g+1)+(g-n%g)*h(n//g))
    result = n_input % g * h(n_input // g + 1) + (g - n_input % g) * h(n_input // g)
    print(result)

if __name__ == "__main__":
    main(10)