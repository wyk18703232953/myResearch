from math import sin, pi

def p(n, r):
    return 2 * n * r * sin(pi / n)

def main(n):
    # 根据规模 n 生成测试数据：r = n（可按需要修改生成规则）
    r = float(n)

    le = 0.0
    ri = r * 1000.0
    m = 0.0
    while ri - le > 1e-9:
        m = (ri + le) / 2.0
        if p(n, r + m) < n * m * 2.0:
            ri = m

        else:
            le = m
    # print(m)
    pass

# 示例调用
if __name__ == "__main__":
    main(10)