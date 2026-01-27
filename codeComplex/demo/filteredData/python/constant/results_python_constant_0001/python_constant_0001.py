from math import sqrt

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
    # 将 n 映射为参数规模：
    # 为保证可扩展与确定性，使用简单算术关系生成参数
    # a, v, l, d, w > 0，且保证 a 非零
    if n < 1:
        n = 1

    # 确定性生成参数
    a = (n % 10) + 1          # 1..10
    v = (n % 100) + 1         # 1..100
    l = n * 10 + 50           # 距离随 n 线性增长
    d = max(1, n * 5)         # 使 d 随 n 线性增长
    w = (n * 3) % 120 + 1     # 1..120，限制速度

    # 为避免 d > l 造成负距离，做一次调整
    if d > l:
        d = l // 2 if l >= 2 else 1

    ans = solve(a, v, l, d, w)
    # print(f"{ans:.8f}")
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以进行规模实验
    main(100000)