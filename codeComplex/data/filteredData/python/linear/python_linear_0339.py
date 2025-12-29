import math
import random

def main(n):
    # 生成测试数据：
    # 1. 生成 d：取 1 到 10 之间的整数
    d = random.randint(1, 10)
    # 2. 生成 n 个递增的点位置 pos
    #    为了避免过大数值，使用累加随机步长构造递增序列
    pos = []
    current = random.randint(-50, 50)
    pos.append(current)
    for _ in range(1, n):
        step = random.randint(1, 20)  # 确保递增
        current += step
        pos.append(current)

    # 原逻辑
    count = 2
    for i in range(1, n):
        if math.fabs(pos[i] - pos[i - 1]) > 2 * d:
            count += 2
        elif math.fabs(pos[i] - pos[i - 1]) == 2 * d:
            count += 1
        else:
            continue

    # 输出结果（可根据需要一起输出测试数据用于验证）
    print(count)

if __name__ == "__main__":
    # 举例执行 main，规模可修改
    main(5)