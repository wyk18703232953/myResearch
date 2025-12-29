import random

def main(n):
    # 参数示例设置：可按需要调整或改为入参
    l = n * 10          # 下界
    r = n * 20          # 上界
    x = max(1, n // 3)  # 难度差最小值

    # 生成测试数据：难度数组 c
    # 让数据分布在 [1, 50]，也可以根据需要调整范围
    random.seed(0)
    c = [random.randint(1, 50) for _ in range(n)]

    # 原逻辑
    ans = 0
    for mask in range(1 << n):
        s = 0
        num = 0
        ma = 0
        mi = 10**9
        for i in range(n):
            if mask & (1 << i):
                num += 1
                s += c[i]
                ma = max(ma, c[i])
                mi = min(mi, c[i])
        if l <= s <= r and ma - mi >= x and num >= 2:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例调用：可修改 n 的值进行不同规模测试
    main(5)