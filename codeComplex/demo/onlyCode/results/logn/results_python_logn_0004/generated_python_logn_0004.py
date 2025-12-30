import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里将 n 作为 a、b 的取值上限
    if n <= 0:
        a = 0
        b = 0
    else:
        a = random.randint(0, n)
        b = random.randint(0, n)

    if a == b:
        print(0)
    else:
        x = a ^ b
        c = 0

        while x:
            x //= 2
            c += 1

        print(2 ** c - 1)


if __name__ == "__main__":
    # 示例：可自行修改 n 的大小
    main(100)