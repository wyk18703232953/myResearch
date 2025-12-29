import random

def main(n):
    # 生成测试数据
    # 难度数组 c：随机 1~1000
    c = [random.randint(1, 1000) for _ in range(n)]
    # 生成 least, most（总难度区间）
    total = sum(c)
    least = random.randint(0, total)
    most = random.randint(least, total)
    # 生成 x（最难与最易差值下界）
    x = random.randint(0, max(c) - min(c) if n > 1 else 0)

    # 原始逻辑
    ans = 0
    _max = lambda x, y: x if x > y else y
    _min = lambda x, y: x if x < y else y

    for mask in range(1 << n):
        mx = float('-inf')
        mn = float('inf')
        count = 0
        Sum = 0
        for i in range(n):
            if mask & (1 << i):
                count += 1
                Sum += c[i]
                mx = _max(mx, c[i])
                mn = _min(mn, c[i])
        if count >= 2 and least <= Sum <= most and mx - mn >= x:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)