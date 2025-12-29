import random
import math

def main(n):
    # 生成测试数据：随机半径 r 和 n 个随机坐标
    # 可根据需要调整数据规模与范围
    r = random.randint(1, 10)
    x_coord = [random.randint(0, 100) for _ in range(n)]

    d = {}
    results = []

    for i in x_coord:
        final = float(r)
        for j in range(i - r, i + r + 1):
            check = d.get(j, [-1, -1])
            if check[0] > 0:
                potential = check[1] + math.sqrt((4 * r * r) - ((i - check[0]) ** 2))
                final = max(potential, final)
        for j in range(i - r, i + r + 1):
            d[j] = (i, final)
        results.append(final)

    # 输出结果以保持与原程序类似的行为
    for v in results:
        print(v)

if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改或在外部调用 main(n)
    main(5)