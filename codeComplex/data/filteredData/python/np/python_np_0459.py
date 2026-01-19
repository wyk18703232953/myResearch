def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h(n, x, y, g):
    return max(f(n, 0, x, y, g), f(n, 1, x, y, g))

def core(n, x, y):
    import math
    g = math.gcd(x, y)
    y2 = y + x
    return n % g * h(n // g + 1, x, y2, g) + (g - n % g) * h(n // g, x, y2, g)

def main(n):
    # 解释输入规模映射（仅作为设计依据，不在输出中说明）：
    # 给定 n，构造一组确定性的 (N, X, Y) 作为原程序的输入：
    # N = n
    # X = n + 1
    # Y = 2 * n + 3
    # 这样三元组完全由 n 决定，可重复、可扩展
    if n <= 0:
        # 对于非正规模，定义为退化情形，返回 0
        print(0)
        return
    N = n
    X = n + 1
    Y = 2 * n + 3
    ans = core(N, X, Y)
    print(ans)

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 进行规模实验
    main(10)