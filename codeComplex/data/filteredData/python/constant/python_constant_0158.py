from math import *

def main(n: int):
    # 原程序逻辑：按给定 n 输出两个数
    if n % 2 == 0:
        print(n - 8, n - (n - 8))
    else:
        print(n - 9, n - (n - 9))


if __name__ == "__main__":
    # 根据 n 生成测试数据：这里只是示例调用，可按需修改 n
    test_n = 20
    main(test_n)