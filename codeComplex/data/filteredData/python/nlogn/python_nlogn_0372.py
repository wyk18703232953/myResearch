from collections import Counter
import random

def main(n):
    # 生成测试数据：
    # 随机生成 k，范围控制在 0~10
    k = random.randint(0, 10)
    # 随机生成 n 个整数，范围控制在 0~20
    arr = [random.randint(0, 20) for _ in range(n)]

    # 原始逻辑开始
    arr.sort()
    f = arr[0]
    p = n
    i = 0
    count = 0
    while i < n:
        while i < n and arr[i] == f:
            i += 1
            count += 1
        if i < n and arr[i] <= f + k:
            p -= count
        if i < n:
            f = arr[i]
            count = 0
        continue

    print(p)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)