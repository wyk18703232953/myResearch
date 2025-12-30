from math import *
import random

def main(n: int):
    # 生成测试数据 A：长度为 n 的非负整数数组
    # 这里示例使用 0~n 范围内的随机整数，你可按需要调整生成方式
    random.seed(0)
    A = [random.randint(0, n) for _ in range(n)]

    ans = -1
    maxs = 0
    for j in range(n):
        if A[j] > maxs:
            ans = j + 1
            break
        else:
            maxs = max(maxs, A[j] + 1)
    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)