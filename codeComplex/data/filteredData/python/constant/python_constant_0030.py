import random

def main(n: int):
    # 根据 n 生成测试数据，这里用 n 本身作为原程序中的输入
    x = n

    # 原逻辑：输入一个整数 n，输出 3*n//2
    result = 3 * x // 2
    print(result)


if __name__ == "__main__":
    # 示例：可修改这里的 n 进行测试
    main(10)