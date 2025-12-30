import random

def main(n):
    # 1. 生成测试数据
    # 难度数组 c：生成 n 个 1~1000 的随机整数
    c = [random.randint(1, 1000) for _ in range(n)]
    c.sort()

    # l, r 为总难度范围，x 为最大与最小难度之差的下限
    total_sum = sum(c)
    l = total_sum // 4 if total_sum >= 4 else 0           # 下界
    r = total_sum // 2 if total_sum >= 2 else total_sum   # 上界
    if l > r:
        l, r = r, l
    x = max(1, (max(c) - min(c)) // 3)  # 至少要求一定的难度跨度

    # 2. 原逻辑计算满足条件的题目集合数量
    ans = 0
    for mask in range(1 << n):
        s = []
        for j in range(n):
            if mask & (1 << j):
                s.append(c[j])
        if not s:
            continue
        total = sum(s)
        if l <= total <= r and max(s) - min(s) >= x:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：运行 n=10
    main(10)