import math

def solutions(a, b, c):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)
    if sol1 < 0 and sol2 > 0:
        return sol2
    elif sol1 > 0 and sol2 < 0:
        return sol1

    else:
        return 0

def main(n):
    # 确定性生成 c, m，使得方程判别式非负，保持算法逻辑
    # 这里令 c = n，m = 2 * n，c 和 m 随 n 线性增长
    c = n
    m = 2 * n
    result = int(c - solutions(1, 3, -(2 * c + 2 * m)))
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，使用一个适中的规模 n
    main(10)