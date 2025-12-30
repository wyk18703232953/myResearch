import random

def main(n: int):
    # 根据 n 生成测试数据，这里示例为生成 n 个随机整数
    test_data = [random.randint(1, 100) for _ in range(n)]
    # 如果需要使用测试数据，可在此处加入处理逻辑
    # 由于原程序只输出 25，这里保持同样行为
    print(25)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)