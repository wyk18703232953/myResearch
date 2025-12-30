import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里示例为：
    # a, b 在 [0, n] 范围内
    # x, y, z 在 [0, n] 范围内
    a = random.randint(0, n)
    b = random.randint(0, n)
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)

    # 原逻辑：print(max(0,2*x+y-a)+max(0,y+3*z-b))
    result = max(0, 2 * x + y - a) + max(0, y + 3 * z - b)
    print(result)

if __name__ == "__main__":
    # 示例：用 n = 10 运行
    main(10)