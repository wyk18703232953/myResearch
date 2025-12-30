import random

def main(n: int):
    # 生成测试数据：p, l, r，满足 1 <= l <= p <= r <= n
    p = random.randint(1, n)
    l = random.randint(1, p)
    r = random.randint(p, n)

    # 原始逻辑
    if l == 1 and r == n:
        ans = 0
    elif l == 1:
        ans = abs(p - r) + 1
    elif r == n:
        ans = abs(p - l) + 1
    else:
        ans = min(abs(p - r), abs(p - l)) + r - l + 2

    print(ans)


if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(10)