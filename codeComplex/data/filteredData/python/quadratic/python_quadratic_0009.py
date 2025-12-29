import math
import random

def main(n):
    # 生成测试数据
    # 固定半径为 1 到 10 之间的随机整数
    radii = random.randint(1, 10)
    # 生成 n 个递增的 x 坐标，步长为 1 到 2*radii 之间的随机值
    x_list = []
    cur = 0
    for _ in range(n):
        step = random.randint(1, 2 * radii)
        cur += step
        x_list.append(cur)

    # 原始逻辑开始
    temp_arr = []
    for i in range(n):
        candidates = [radii]
        for j in range(i):
            if abs(x_list[i] - x_list[j]) <= 2 * radii:
                height = math.sqrt(4 * radii ** 2 - (x_list[i] - x_list[j]) ** 2) + temp_arr[j]
                candidates.append(height)
        temp_arr.append(max(candidates))

    for v in temp_arr:
        print(v, end=" ")
    print()  # 换行，便于多次调用时阅读

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)