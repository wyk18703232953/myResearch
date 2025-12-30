from math import ceil
import random

def paper(a, b, c, d):
    return ceil((a * (ceil(b / c))) / d)

def main(n):
    # 根据 n 生成测试数据，示例：参数在 1 ~ n 范围内的随机整数
    a = random.randint(1, n)
    b = random.randint(1, n)
    c = random.randint(1, n)
    d = random.randint(1, n)
    result = paper(a, b, c, d)
    print(result)

if __name__ == "__main__":
    # 示例：运行规模 n=100
    main(100)