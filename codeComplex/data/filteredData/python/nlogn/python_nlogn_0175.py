import random

def main(n: int):
    # 生成测试数据：n 组 (xx, ww)
    # 这里假设坐标与半径范围为 [-10^9, 10^9]
    # 可以根据需要调整数据范围
    d = []
    for _ in range(n):
        xx = random.randint(-10**9, 10**9)
        ww = random.randint(0, 10**9)
        d.append([xx - ww, xx + ww])

    # 按左端点排序
    d.sort(key=lambda x: x[0])

    last = -10**12
    ans = 0
    for i in range(n):
        if last <= d[i][0]:
            last = d[i][1]
            ans += 1
        elif last > d[i][1]:
            last = d[i][1]

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)