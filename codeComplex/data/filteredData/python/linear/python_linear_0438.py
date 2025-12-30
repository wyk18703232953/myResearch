import math
import random

def main(n: int):
    # 根据 n 生成测试数据，这里直接使用 1..n 的顺序数组作为测试数据
    A = [i + 1 for i in range(n)]

    x = int(math.sqrt(n))
    # 分块
    X = [A[i:i + x] for i in range(0, len(A), x)]
    # 块逆序
    X = X[::-1]
    # 展平
    f = [item for sublist in X for item in sublist]
    print(*f)


if __name__ == "__main__":
    # 示例：可自行修改 n 观察输出
    main(10)