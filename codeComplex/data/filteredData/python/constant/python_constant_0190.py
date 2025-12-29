import random

def main(n: int):
    # 根据 n 生成测试数据，这里仅示例生成一个长度为 n 的随机数组
    test_data = [random.randint(1, 100) for _ in range(n)]
    # 如有需要可使用 test_data 做后续处理
    # 当前原始逻辑只输出固定的 '25'
    print('25')


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时由外部指定 n
    main(10)