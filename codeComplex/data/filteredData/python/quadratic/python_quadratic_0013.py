import math
import random

def main(n):
    r = 1  # 半径可按需调整
    # 生成测试数据：n 个严格递增的横坐标，间距随机
    x = []
    cur = 0
    for _ in range(n):
        cur += random.randint(1, 5)
        x.append(cur)

    y = [r]
    for i in range(1, n):
        _y = r
        for j in range(i):
            if 4 * r * r >= (x[i] - x[j]) * (x[i] - x[j]):
                _y = max(
                    _y,
                    y[j] + math.sqrt(4 * r * r - (x[i] - x[j]) * (x[i] - x[j]))
                )
        y.append(_y)

    print(' '.join(map(str, y)))
    return y

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)