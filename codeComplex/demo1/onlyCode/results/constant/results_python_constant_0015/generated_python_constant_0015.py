def func(u, v, a, l):
    if (v ** 2 - u ** 2) >= 2 * a * l:
        return ((u ** 2 + 2 * a * l) ** 0.5 - u) / a
    else:
        t1 = (v - u) / a
        t2 = (l - (u * t1 + a * t1 * t1 / 2)) / v
        return t1 + t2


def efficient(v, a, w, d):
    if 2 * v * v - w * w <= 2 * a * d:
        t1 = v / a
        t2 = (v - w) / a
        t3 = (d - 0.5 * a * t1 * t1 - v * t2 + 0.5 * a * t2 * t2) / v
        return t1 + t2 + t3
    else:
        bound = ((2 * a * d + w * w) / 2) ** 0.5
        t1 = bound / a
        t2 = (bound - w) / a
        # 原代码中这里有逻辑错误：先 return t1+t2，再 return min(...)
        # 保留原意应为取两种方案中较小的时间
        t3 = func(0, w, a, d)
        return min(t1 + t2, t3)


def main(n):
    """
    n 为规模参数，用来生成测试数据：
      - a: 加速度，取 n 的一个函数，至少为 1
      - v: 最大速度，与 n 成比例
      - l: 总路程，规模为 n
      - d: 约束路段长度，不超过 l
      - w: 在约束点的限速，不超过 v
    返回值为原 main() 中打印的时间结果（float）
    """
    # 确保 n 至少为 1，避免出现 0 加速度等问题
    n = max(1, int(n))

    # 生成一组与 n 规模相关、但不全相同的参数
    a = max(1, n // 5 + 1)      # 加速度
    v = n * 2 + 5               # 最大速度
    l = n * 10 + 20             # 总路程
    d = max(1, min(l - 1, n * 3))  # 有约束的路段长度
    w = max(1, min(v - 1, n + 3))  # 约束速度

    if 2 * a * d <= w ** 2 or v <= w:
        t1 = func(0, v, a, l)
        return t1
    else:
        t1 = efficient(v, a, w, d)
        t2 = func(w, v, a, l - d)
        return t1 + t2


if __name__ == "__main__":
    # 示例：用 n = 10 运行一次
    result = main(10)
    print(f"{result:.8f}")