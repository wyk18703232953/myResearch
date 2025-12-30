import random

def main(n):
    # 生成测试数据：
    # n: 规模，由外部传入
    # p, l, r: 在 [1, n] 内随机生成，且保证 l <= r
    p = random.randint(1, n)
    l = random.randint(1, n)
    r = random.randint(1, n)
    if l > r:
        l, r = r, l

    # 原逻辑
    if l == 1 and r == n:
        ans = 0
    elif l == 1:
        ans = abs(p - r) + 1
    elif r == n:
        ans = abs(p - l) + 1
    else:
        ans = min(abs(p - r), abs(p - l)) + r - l + 2

    print(n, p, l, r, "=>", ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)