def f(n, s, y, g, x):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def solve(n, x, y):
    import math
    g = math.gcd(x, y)
    h = lambda nn: max(f(nn, 0, y + x, g, x), f(nn, 1, y + x, g, x))
    y2 = y + x
    return n % g * h(n // g + 1) + (g - n % g) * h(n // g)

def main(n):
    # 将 n 映射为三个参数 (N, X, Y)，与原程序输入结构一致
    # 确定性构造：简单线性与取模映射，保证正整数
    N = max(1, n)
    X = max(1, 2 * n + 1)
    Y = max(1, 3 * n + 2)
    # 保证 gcd(X, Y + X) 不为 0，也不会引入非确定性
    return solve(N, X, Y)

if __name__ == "__main__":
    # 示例调用：使用固定的 n 进行一次确定性运行
    result = main(10)
    print(result)