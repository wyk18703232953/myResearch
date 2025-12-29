import random

def main(n: int):
    # 根据 n 生成测试数据，这里假设原题中 n 的输入范围为 [1, n]
    # 我们随机生成一个测试值 test_n 作为原程序中的输入
    if n <= 0:
        return

    test_n = random.randint(1, n)

    # 原程序逻辑开始（将 input() 替换为 test_n）
    val = test_n + 1
    if val == 1:
        print(0)
        return
    print(val if val % 2 else val // 2)

if __name__ == "__main__":
    # 示例：调用 main，规模可在这里修改
    main(10)