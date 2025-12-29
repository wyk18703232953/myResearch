import math
import random

def main(n):
    # 根据规模 n 生成测试数据 (l, r)
    # 这里示例：生成一个区间长度约为 n，且保证 l < r
    # 你可以按需要修改生成策略
    if n < 3:
        n = 3

    l = random.randint(1, 10)
    r = l + n  # 区间长度约为 n

    # 原始逻辑开始
    a = l
    if a % 2:
        a += 1

    if a + 2 > r:
        print(-1)
    else:
        print(a, a + 1, a + 2)

if __name__ == "__main__":
    # 示例调用
    main(10)