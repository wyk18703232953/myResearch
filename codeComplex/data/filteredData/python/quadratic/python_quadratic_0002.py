import random
import math

def main(n):
    # 生成测试数据：随机半径 r 和 n 个坐标 x
    # 可根据需要调整数据生成策略
    r = random.randint(1, 10)
    x = [random.randint(-10 * n, 10 * n) for _ in range(n)]

    y = [r] * n
    for i in range(1, n):
        for j in range(i):
            d = abs(x[i] - x[j])
            if d <= 2 * r:
                y[i] = max(y[i], y[j] + math.sqrt(4 * r * r - d * d))
    print(*y)

if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可根据需要修改 n
    main(5)