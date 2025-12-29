import random

def main(n: int):
    # 根据 n 生成测试数据，这里示例为生成 n 个 1~100 的随机整数
    data = [random.randint(1, 100) for _ in range(n)]
    # 原逻辑仅打印 25，这里保持原始逻辑不变
    print(25)

if __name__ == "__main__":
    # 示例：调用 main，规模设置为 10
    main(10)