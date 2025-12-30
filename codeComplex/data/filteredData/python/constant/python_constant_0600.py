import math
import random

def main(n):
    # 生成测试数据：n 和 k
    # 这里假设 k 在 1 到 10 之间生成，可根据需要调整
    k = random.randint(1, 10)

    a = [2, 5, 8]
    s = 0
    for i in a:
        s += (n * i - 1) // k + 1
    print(s)

if __name__ == "__main__":
    # 示例调用：可自行修改 n 的值
    main(10)