import math
import random

def main(n):
    # 生成测试数据
    # n: 线段数量
    # t: 间隔阈值，设为 1 到 10 之间的整数
    t = random.randint(1, 10)
    segments = []
    for _ in range(n):
        # 生成 a,b，保证 b >= 0
        a = random.randint(-100, 100)
        b = random.randint(0, 20)
        segments.append((a, b, t))

    # 原逻辑开始（不再使用 input）
    l = []
    # 只用第一条生成的 (a,b) 的 t 作为全局 t（与原代码一致：n,t 一行给出）
    t = segments[0][2]
    for a, b, _ in segments:
        x = a - b / 2
        y = a + b / 2
        l.append([x, y])

    l.sort()
    c = 0
    for i in range(n - 1):
        diff = l[i + 1][0] - l[i][1]
        if diff > t:
            c += 2
        elif diff == t:
            c += 1
    result = c + 2

    print(result)

if __name__ == "__main__":
    # 示例：n = 5
    main(5)