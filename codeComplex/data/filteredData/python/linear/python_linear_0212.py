from collections import defaultdict
import random

def main(n):
    # 生成测试数据
    # a, b 为任意整数（原代码中 b 实际未使用，这里仍然生成）
    a = random.randint(-5, 5)
    b = random.randint(-5, 5)

    XV = []
    for _ in range(n):
        # 生成 x, vx, vy，范围可按需调整
        x = random.randint(-10**6, 10**6)
        vx = random.randint(-10**3, 10**3)
        vy = random.randint(-10**3, 10**3)
        XV.append((x, vx, vy))

    if a != 0:
        ans = 0
        d = defaultdict(int)
        dvx = defaultdict(int)
        dvy = defaultdict(int)
        dvxy = defaultdict(int)
        for x, vx, vy in XV:
            k = -a * vx + vy
            ans += max(0, d[k] - (dvx[(k, vx)] + dvy[(k, vy)] - dvxy[(k, vx, vy)]))
            d[k] += 1
            dvx[(k, vx)] += 1
            dvy[(k, vy)] += 1
            dvxy[(k, vx, vy)] += 1
        print(ans * 2)
    else:
        ans = 0
        d = defaultdict(lambda: defaultdict(int))
        ds = defaultdict(int)
        for x, vx, vy in XV:
            ans += max(0, ds[vy] - d[vy][vx])
            d[vy][vx] += 1
            ds[vy] += 1
        print(ans * 2)


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)