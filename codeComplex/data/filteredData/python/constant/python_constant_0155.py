import random

def main(n: int):
    # 根据 n 生成测试数据，这里直接使用传入的 n 作为测试规模
    # 如果需要随机测试数据，可改为：n = random.randint(1, 10**6)
    
    if n % 2 == 0:
        print(4, n - 4)
    else:
        print(9, n - 9)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可在外部按需调用 main(n)
    main(10)