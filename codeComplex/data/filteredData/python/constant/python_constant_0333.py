import random

def main(n):
    # 这里的 n 既作为规模，也作为要处理的数
    # 若希望用随机生成的测试数据，可将 n 替换为随机值
    # 例如：x = random.randint(0, n)
    x = n

    if x == 0:
        print(0)
    else:
        if x % 2 == 0:
            print(x + 1)
        else:
            print((x + 1) // 2)


if __name__ == "__main__":
    # 示例：选择一个规模 n，调用 main(n)
    # 例如：n = 10，可以改为任何正整数
    n = 10
    main(n)