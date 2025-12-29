import random

def main(n: int):
    # 根据规模 n 生成测试数据，控制区间大小约为 2^n
    # 保证 0 <= l <= r < 2^n，且 n 限制在 [1, 60] 之间防止移位过大
    n = max(1, min(n, 60))
    max_val = (1 << n) - 1
    l = random.randint(0, max_val)
    r = random.randint(l, max_val)

    # 原始逻辑
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
    # 示例：调用 main(10)，可根据需要修改规模
    main(10)