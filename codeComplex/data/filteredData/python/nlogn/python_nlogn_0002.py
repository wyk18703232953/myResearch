import math
import random

def main(n):
    # 生成测试数据：
    # n 行 (a, b)，a 为 0~1000 的随机整数，b 为 0~100 的随机正整数
    # t 为 0~100 的随机整数
    t = random.randint(0, 100)
    ab_pairs = []
    for _ in range(n):
        a = random.randint(0, 1000)
        b = random.randint(1, 100)
        ab_pairs.append((a, b))

    # 原逻辑开始（移除 input，使用生成的数据）
    segments = []
    for a, b in ab_pairs:
        x = a - b / 2
        y = a + b / 2
        segments.append([x, y])

    segments.sort()
    c = 0
    for i in range(n - 1):
        diff = segments[i + 1][0] - segments[i][1]
        if diff > t:
            c += 2
        elif diff == t:
            c += 1

    result = c + 2
    print(result)

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(5)