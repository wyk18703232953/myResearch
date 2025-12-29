from math import ceil
import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里示例：
    # k 在 [1, max(1, n)] 范围内随机生成
    k = random.randint(1, max(1, n))

    cou = 0
    cou += ceil(n * 2 / k)
    cou += ceil(n * 5 / k)
    cou += ceil(n * 8 / k)
    print(cou)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(10)