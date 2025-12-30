import random

def main(n: int):
    # 这里的 n 用作规模参数，用于生成测试数据
    # 原逻辑只与单个整数输入有关，因此从规模 n 中派生一个测试值
    # 例如：生成一个 1 到 max(2, n) 之间的随机整数作为输入
    test_value = random.randint(1, max(2, n))

    # 原始逻辑：如果输入为 1，则输出 5，否则输出 25
    if test_value == 1:
        print(5)
    else:
        print(25)

# 示例：手动调用
# main(10)