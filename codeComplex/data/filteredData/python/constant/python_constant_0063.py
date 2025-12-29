import random

def main(n):
    # 根据规模 n 生成测试数据，这里理解为生成一个整数 x
    # 你可以根据需要修改数据生成逻辑，如范围、分布等
    x = random.randint(0, max(1, n))

    # 保持原程序逻辑：输出 "0 0 x"
    print(0, 0, x)

if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)