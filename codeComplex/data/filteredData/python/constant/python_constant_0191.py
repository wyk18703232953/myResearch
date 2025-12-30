import random

def main(n: int):
    # 根据 n 生成测试数据（示例：生成 n 个 1..100 的随机整数）
    test_data = [random.randint(1, 100) for _ in range(n)]
    # 原程序逻辑与 n 无关，只输出 25
    print(25)

if __name__ == "__main__":
    # 示例：调用 main，规模可在此调节
    main(10)