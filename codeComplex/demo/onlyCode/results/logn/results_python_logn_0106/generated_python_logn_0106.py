import random

def main(n: int):
    # 根据规模 n 生成测试数据，约束 a, b 的大小
    # 可按需求调整范围，这里让 a, b 与 n 同级别
    a = random.randint(0, n)
    b = random.randint(0, n)

    c = 1
    result = a ^ b
    while c <= result:
        c *= 2
    c -= 1

    print(c)


if __name__ == "__main__":
    # 示例：规模设为 100
    main(100)