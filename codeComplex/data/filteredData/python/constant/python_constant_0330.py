import sys
import random

def main(n):
    # n 作为规模，这里直接用 n 作为原程序中的输入
    if n == 0:
        print(0)
        return
    if (n + 1) % 2 == 0:
        print((n + 1) // 2)
    else:
        print(n + 1)

if __name__ == "__main__":
    # 示例：根据规模生成一个测试数据
    # 这里的策略是：在 [0, n] 范围内随机生成一个整数作为测试输入
    test_n = 0
    if len(sys.argv) > 1:
        # 若从命令行传入规模，则使用它生成测试数据
        scale = int(sys.argv[1])
        test_n = random.randint(0, scale)
    else:
        # 未传入规模，则使用一个默认规模 100 生成测试数据
        scale = 100
        test_n = random.randint(0, scale)

    main(test_n)