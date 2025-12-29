import random

def main(n: int):
    # 根据 n 生成测试数据，这里示例为生成 n 个 1~100 的随机整数
    test_data = [random.randint(1, 100) for _ in range(n)]
    # 原程序只输出一个常数，这里仍保持核心行为
    print(25)
    # 若需要使用生成的数据，可在此处扩展逻辑
    # 比如：print(test_data)

if __name__ == "__main__":
    # 示例调用，规模可在此修改
    main(10)