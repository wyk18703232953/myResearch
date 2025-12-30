import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里示例：a,d,y,g,b 都在 [0, n] 范围内随机生成
    a = random.randint(0, n)
    d = random.randint(0, n)
    y = random.randint(0, n)
    g = random.randint(0, n)
    b = random.randint(0, n)

    m = y * 2 + g
    nn = b * 3 + g
    c = 0
    if m > a:
        c += m - a
    if nn > d:
        c += nn - d

    print(c)


if __name__ == "__main__":
    # 可自行修改 n 的默认值
    main(10)