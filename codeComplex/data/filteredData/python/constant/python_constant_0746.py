import random

def main(n: int):
    # 生成测试数据，这里直接使用传入的 n 作为规模
    # 若需要批量测试，可在此处按需生成多个 n 值
    ans = n * n + (n - 1) * (n - 1)
    print(ans)


if __name__ == "__main__":
    # 示例：根据规模上限随机生成一个 n 进行测试
    # 你也可以直接指定 n = 某个值
    max_n = 100
    test_n = random.randint(1, max_n)
    main(test_n)