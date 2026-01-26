import sys
from collections import defaultdict

def main(n):
    # 确定性参数生成
    # a 在 [-2, -1, 0, 1, 2] 中循环
    a_values = [-2, -1, 0, 1, 2]
    a = a_values[n % len(a_values)]
    # b 参与输入但未使用，固定为 0
    b = 0

    # 生成 XV：长度为 n 的 (x, vx, vy) 三元组列表
    XV = []
    for i in range(n):
        x = i
        vx = (i * 2) % (n + 1)  # 避免除零并保持确定性
        vy = (i * 3 + 1) % (n + 2)
        XV.append((x, vx, vy))

    if a != 0:
        ans = 0
        d = defaultdict(lambda: 0)
        dvx = defaultdict(lambda: 0)
        dvy = defaultdict(lambda: 0)
        dvxy = defaultdict(lambda: 0)
        for x, vx, vy in XV:
            k = -a * vx + vy
            ans += max(0, d[k] - (dvx[(k, vx)] + dvy[(k, vy)] - dvxy[(k, vx, vy)]))
            d[k] += 1
            dvx[(k, vx)] += 1
            dvy[(k, vy)] += 1
            dvxy[(k, vx, vy)] += 1
        # print(ans * 2)
        pass

    else:
        ans = 0
        d = defaultdict(lambda: defaultdict(lambda: 0))
        ds = defaultdict(lambda: 0)
        for x, vx, vy in XV:
            ans += max(0, ds[vy] - d[vy][vx])
            d[vy][vx] += 1
            ds[vy] += 1
        # print(ans * 2)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)