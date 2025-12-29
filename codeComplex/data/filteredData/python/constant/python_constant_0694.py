from math import sin
import random

def main(n: int):
    """
    根据规模 n 生成测试数据并计算结果：
    原逻辑为：
        输入: n, r
        输出: r / ((2*sin(pi*(1/2-1/n)))/(sin(2*pi/n)) - 1)
    这里：n 由参数传入，r 由测试数据生成。
    """
    # 生成测试数据 r，这里设为与 n 同量级的随机正整数
    # 你可以根据需要修改生成规则
    random.seed(0)  # 固定随机种子，结果可复现
    r = random.randint(1, max(1, 10 * n))

    pi = 3.14159265359
    denominator = (2 * sin(pi * (1 / 2 - 1 / n))) / (sin(2 * pi / n)) - 1
    result = r / denominator
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)