from math import sqrt
import random

def findt(u, v, a, dist):
    front = (v * v - u * u) / (2 * a)
    if front > dist:
        return (sqrt(u * u + 2 * a * dist) - u) / a
    return (v - u) / a + (dist - front) / v

def solve(a, v, l, d, w):
    if v <= w or 2 * a * d <= w * w:
        return findt(0, v, a, l)
    after = findt(w, v, a, l - d)
    peak = sqrt(a * d + w * w / 2)
    if peak > v:
        travel = (v * v - w * w / 2) / a
        before = (2 * v - w) / a + (d - travel) / v
    else:
        before = (2 * peak - w) / a
    return before + after

def main(n):
    # 根据规模 n 生成测试数据
    # 假设 n 表示道路总长度 l 的大致规模
    random.seed(n)

    a = random.randint(1, 10)            # 加速度
    v = random.randint(1, 50)            # 最大速度
    l = max(1, n)                        # 总长度，不小于 1
    d = random.randint(1, max(1, l - 1)) # 限速区结束位置
    w = random.randint(1, 50)            # 限速

    ans = solve(a, v, l, d, w)
    print(f"{ans:.8f}")

if __name__ == "__main__":
    # 示例：使用 n=100 运行一次
    main(100)