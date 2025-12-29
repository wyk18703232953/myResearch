import random

def main(n: int):
    # 根据规模 n 生成测试数据大小（这里简单与 n 关联，可按需调整）
    # 假设 a,b,x,y,z 的值范围随 n 增大而增大
    max_val = max(1, n * 10)

    # 生成测试数据
    a = random.randint(0, max_val)
    b = random.randint(0, max_val)
    x = random.randint(0, max_val)
    y = random.randint(0, max_val)
    z = random.randint(0, max_val)

    # 原始逻辑
    yell = 2 * x + y
    blue = y + 3 * z
    res = max(0, yell - a) + max(0, blue - b)

    # 输出结果
    print(res)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)