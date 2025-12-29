import random

def main(n):
    # 根据 n 生成测试数据，这里直接使用传入的 n 作为测试值
    # 如果需要批量测试，可以自行在外层多次调用 main 或扩展逻辑

    if n % 2 == 0:
        a = n - 8
        print(a, 8)
    else:
        a = n - 9
        print(a, 9)


if __name__ == "__main__":
    # 示例：可根据需要修改或批量调用
    test_n = 20  # 示例测试规模
    main(test_n)