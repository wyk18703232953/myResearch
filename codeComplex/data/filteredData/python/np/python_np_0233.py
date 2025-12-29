import random

def main(n):
    # 生成测试数据
    # 随机生成题目难度 c[i]，范围 1~10^6
    c = [random.randint(1, 10**6) for _ in range(n)]
    total_sum = sum(c)

    # 生成合理的 l, r, x（保证有一定概率存在解）
    # 设 x 为难度至少差 1/4 最大差值
    max_diff = max(c) - min(c)
    x = max(1, max_diff // 4)

    # 设 l, r 为总难度的一段区间
    # 下界是总和的 1/4，上界是总和的 3/4（做整数截断）
    l = total_sum // 4
    r = (total_sum * 3) // 4
    if l > r:
        l, r = r, l  # 防止反转

    ans = 0
    # 枚举所有非空子集
    for mask in range(1 << n):
        a = []
        for bit in range(n):
            if mask & (1 << bit):
                a.append(c[bit])
        if len(a) >= 2:
            sa = sum(a)
            if l <= sa <= r and max(a) - min(a) >= x:
                ans += 1

    print(ans)

# 示例运行（例如 n=10）
if __name__ == "__main__":
    main(10)