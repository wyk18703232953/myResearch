import random

def main(n: int):
    # 根据 n 生成测试数据，这里将 n 作为数值上界
    # 生成 [0, n] 范围内的随机 l, r 并保证 l <= r
    if n < 0:
        raise ValueError("n must be non-negative")
    l = random.randint(0, n)
    r = random.randint(l, n)

    # 原逻辑
    for i in range(63, -1, -1):
        mx, mn = r, l
        if (1 << i) & l and (1 << i) & r:
            mx = (1 << i) - 1
            mx = (r ^ (1 << i)) | mx
        elif ((1 << i) & l) == 0 and ((1 << i) & r) == 0:
            mn = (1 << i) - 1
            mn = (l & mn) ^ (l | (1 << i))
        if mx >= l and mx <= r and mn >= l and mn <= r:
            r, l = mx, mn
    print(l ^ r)

if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)