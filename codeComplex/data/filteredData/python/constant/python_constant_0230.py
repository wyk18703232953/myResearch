import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里示例：a,b,x,y,z 的范围随 n 线性放大
    a = random.randint(0, n * 10)
    b = random.randint(0, n * 10)
    x = random.randint(0, n * 5)
    y = random.randint(0, n * 5)
    z = random.randint(0, n * 5)

    needa = 2 * x + y
    needb = y + 3 * z
    result = max(0, needa - a) + max(0, needb - b)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要调整
    main(10)