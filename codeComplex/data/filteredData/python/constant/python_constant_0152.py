import random

def main(n: int):
    # 根据 n 生成测试数据，这里直接用传入的 n 作为测试数据
    # 如需随机测试，可改为: n = random.randint(1, 10**6)

    if n % 2 == 0:
        print(n - 4, "4")
    else:
        print(n - 9, "9")


if __name__ == "__main__":
    # 示例：可在此处修改 n 进行简单测试
    test_n = 20
    main(test_n)