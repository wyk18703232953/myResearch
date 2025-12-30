import math
import random

def main(n):
    # 根据规模 n 生成测试数据
    # 原程序中还需要一个 m，这里随机生成一个较大的整数作为测试数据
    # 也可以根据需要修改生成方式
    m = random.randint(0, 10**9)

    if n >= 27:
        print(m)
    else:
        print(m % (2 ** n))


if __name__ == "__main__":
    # 示例调用：可以在此处修改 n 来测试不同规模
    main(10)