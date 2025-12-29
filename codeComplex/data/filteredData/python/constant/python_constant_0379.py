import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里示例生成：
    #   a, b 在 [0, n] 范围内
    #   c 在 [0, min(a, b)] 范围内，以增加生成合理数据的概率
    a = random.randint(0, n)
    b = random.randint(0, n)
    c = random.randint(0, min(a, b))

    # 原始逻辑
    p = a + b - c
    f = n - p
    if p >= n or c > a or c > b:
        print("-1")
    else:
        print(f)

# 示例：当作为脚本运行时，可指定一个规模
if __name__ == "__main__":
    main(10)