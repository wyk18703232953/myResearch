import math
import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 约定：r 为 [1, n] 范围内的随机整数
    if n <= 2:
        raise ValueError("n 必须大于 2 才有意义")

    r = random.randint(1, n)

    s = math.sin(math.pi / n)
    result = r * s / (1 - s)
    print(f"{result:.7f}")

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)