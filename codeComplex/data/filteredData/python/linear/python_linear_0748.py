import math
import sys
import random

def main(n):
    # 原逻辑：根据 n 计算结果
    r = 0
    t = 1
    for _ in range(n - 1):
        r += t * 2
        t += 2
    result = r + t

    # 根据 n 生成测试数据（这里简单示例：生成一个长度为 n 的整数数组）
    test_data = [random.randint(1, 100) for _ in range(n)]

    # 输出结果（可根据需要调整输出内容）
    print("n =", n)
    print("result =", result)
    print("test_data =", test_data)


if __name__ == "__main__":
    # 示例：调用 main，n 可在此处修改或由外部调用 main(n)
    main(10)