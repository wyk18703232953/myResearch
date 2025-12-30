import random

def main(n: int):
    # 根据 n 生成测试数据（这里仅示例生成一个长度为 n 的随机数组）
    test_data = [random.randint(1, 100) for _ in range(n)]
    # 原逻辑与输入无关，仅输出 25
    print(25)

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)