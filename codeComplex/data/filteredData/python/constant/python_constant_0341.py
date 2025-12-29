import random

def main(n: int):
    # 根据 n 生成测试数据，这里假设原程序的输入规模就是一个整数 n
    # 可根据需要修改为随机或特定策略，这里直接使用参数 n 作为测试数据
    x = n

    # 对应原始逻辑：n = int(input()) + 1
    n_val = x + 1

    if n_val == 1:
        print(0)
    elif n_val % 2:
        print(n_val)
    else:
        print(n_val // 2)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)