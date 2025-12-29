from heapq import heappush, heappop
import random

def main(n):
    # 生成测试数据
    # 随机生成参数 x, y 和 n 个区间 [u, v]
    random.seed(n)  # 使相同 n 下结果可复现
    x = random.randint(1, 10**6)
    y = random.randint(1, 10**6)

    a, b = [], []

    # 生成 n 个区间，u < v，坐标适当控制规模
    for _ in range(n):
        u = random.randint(0, 10**6)
        v = random.randint(u + 1, u + random.randint(1, 10**6))
        a.append((u, 1))
        a.append((v, -1))

    # 以下为原逻辑
    a.sort(key=lambda x: x[0] * 10000000000 - x[1])
    mod = 10 ** 9 + 7
    t, z, ans = 1, 1, x
    for i in range(1, len(a)):
        z += a[i][1]
        if z < t:
            ans = (ans + t * (a[i][0] - a[i - 1][0]) * y) % mod
            heappush(b, -a[i][0])
        else:
            if b:
                if x < (a[i][0] + b[0]) * y:
                    ans = (ans + t * (a[i][0] - a[i - 1][0]) * y + x) % mod
                else:
                    ans = (ans + t * (a[i][0] - a[i - 1][0]) * y + (a[i][0] + b[0]) * y) % mod
                    heappop(b)
            else:
                ans = (ans + t * (a[i][0] - a[i - 1][0]) * y + x) % mod
        t = z

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模为 5
    main(5)