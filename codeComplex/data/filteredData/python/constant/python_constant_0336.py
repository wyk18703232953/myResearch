import random

def main(n: int):
    # 根据 n 生成测试数据，这里假设原程序的输入是一个整数 n_self
    # 可根据需要修改测试数据生成策略
    n_self = random.randint(0, max(1, n))

    if n_self == 0:
        result = 0
    elif n_self % 2 != 0:
        result = (n_self + 1) // 2
    else:
        result = n_self + 1

    print(result)


if __name__ == "__main__":
    # 示例调用：规模参数为 10
    main(10)