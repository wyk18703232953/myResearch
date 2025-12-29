import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里示例为：a,b,x,y,z 都在 [0, n] 范围内随机生成
    a = random.randint(0, n)
    b = random.randint(0, n)
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)

    if a < x * 2 + y:
        ry = x * 2 + y - a
    else:
        ry = 0

    if b < y + z * 3:
        rb = y + z * 3 - b
    else:
        rb = 0

    print(ry + rb)


if __name__ == "__main__":
    # 示例：可以在此处调用 main，并指定规模 n
    main(100)