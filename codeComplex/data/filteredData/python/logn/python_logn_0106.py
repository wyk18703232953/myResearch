import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 让 a、b 的范围随 n 增长，这里简单设定为 [0, n]
    a = random.randint(0, n)
    b = random.randint(0, n)

    c = 1
    # 原代码使用的是按位异或 ^
    result = a ^ b
    while c <= result:
        c *= 2
    c -= 1

    print(c)

if __name__ == "__main__":
    # 示例：可自由修改 n 的值用于测试
    main(10)