import random

def main(n):
    # 生成测试数据
    # 约束：1 <= n，m 为可控参数，这里取 m = n
    m = n

    # 生成 n 个随机整数，范围可根据需要调整
    # 为保证有意义，这里取 [0, n] 区间
    a = [random.randint(0, n) for _ in range(n)]

    # 原始逻辑
    a.sort()
    ans = 0
    cur = 0
    for b in a:
        if b > cur:
            ans += 1
            cur += 1
        else:
            ans += 1
    result = sum(a) - (ans + max(a) - cur)

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)