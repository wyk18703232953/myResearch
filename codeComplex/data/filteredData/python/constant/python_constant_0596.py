import math
import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里假设 N = n，K 取 1~10 之间的随机整数（至少为 1）
    N = n
    K = random.randint(1, 10)

    Rcnt = N * 2
    Gcnt = N * 5
    Bcnt = N * 8

    res = (Rcnt + K - 1) // K + (Gcnt + K - 1) // K + (Bcnt + K - 1) // K
    print(res)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(10)