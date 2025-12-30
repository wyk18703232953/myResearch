from collections import defaultdict
import random

def main(n):
    # 生成测试数据
    # a, b 任选，这里让 a 随机为 0 或非 0，以覆盖两种分支
    a = random.choice([0, 1])
    b = random.randint(-10, 10)

    XV = []
    for _ in range(n):
        x = random.randint(-10**6, 10**6)
        vx = random.randint(-10**3, 10**3)
        vy = random.randint(-10**3, 10**3)
        XV.append((x, vx, vy))

    if a != 0:
        ans = 0
        d = defaultdict(int)
        dvx = defaultdict(int)
        for x, vx, vy in XV:
            k = -a * vx + vy
            ans += max(0, d[k] - dvx[(k, vx)])
            d[k] += 1
            dvx[(k, vx)] += 1
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
    # 示例：规模为 10
    main(10)