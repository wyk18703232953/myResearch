import random

def main(n: int):
    # 根据 n 生成测试数据，这里简单设为原程序中的输入值
    # 原程序使用的是：n_input = int(input()); n = n_input + 1
    # 为了体现“规模 n”，这里将原始输入设置为 n，内部仍然 +1 与原逻辑保持一致
    n_input = n
    n_val = n_input + 1

    # 原逻辑：
    # print(0 if not (n-1) else n//2 if not n&1 else n)
    if not (n_val - 1):
        result = 0
    else:
        if not (n_val & 1):
            result = n_val // 2
        else:
            result = n_val

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)