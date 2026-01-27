from math import tan, pi

def solve(a, b, c):
    D = b * b - 4 * a * c
    k = D ** 0.5
    x1 = (-b + k) / (2 * a)
    x2 = (-b - k) / (2 * a)
    return max(x1, x2)

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里固定 r = n，保持与原题含义类似（r 为半径）
    r = float(n)

    a = (1 / tan(pi / n)) ** 2
    b = -2 * r
    c = -(r * r)
    ans = solve(a, b, c)
    # print(f"{ans:.10f}")
    pass
if __name__ == "__main__":
    # 示例：调用 main(6) 或任意正整数规模
    main(6)