import math
import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 约定：k 在 [1, 2n] 范围内随机生成，确保有一定多样性
    if n <= 0:
        return 0

    k = random.randint(1, max(1, 2 * n))

    # 原逻辑开始
    if k % 2 == 1:
        mink = (k + 1) // 2
    else:
        mink = k // 2 + 1

    result = max(0, min(k - 1, n) - mink + 1)

    # 输出结果（可根据需要也输出生成的 k）
    print(result)
    return result

if __name__ == "__main__":
    # 示例：给定一个规模 n 执行
    main(10)