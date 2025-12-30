import random

def main(n: int):
    # 这里根据 n 生成测试数据，本例原程序只读一个整数 n
    # 我们可以让“规模 n”本身作为原程序的输入值
    value = n

    # 原逻辑：读入一个整数 n，然后输出 "n 0 0"
    print(value, 0, 0)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)