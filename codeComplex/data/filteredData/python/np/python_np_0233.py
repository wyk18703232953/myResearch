def main(n):
    # 参数规模设定：
    # n: 题目数量规模
    # 生成规则完全确定：c[i] = i + 1
    if n <= 0:
        return 0

    c = [i + 1 for i in range(n)]
    total_sum = n * (n + 1) // 2

    # 设定一个确定性的 (l, r, x) 区间
    # l: 下三角和比例
    # r: 上三角和比例
    # x: 最小难度差
    # 所有都由 n 的简单算术确定
    l = total_sum // 4
    r = (total_sum * 3) // 4
    if l > r:  # 理论上不会发生，但保持算法健壮
        l, r = r, l
    x = max(1, n // 4)

    ans = 0
    for mask in range(1 << n):
        a = []
        for bit in range(n):
            if mask & (1 << bit):
                a.append(c[bit])
        if len(a) >= 2 and max(a) - min(a) >= x and l <= sum(a) <= r:
            ans += 1
    return ans


if __name__ == "__main__":
    # 示例调用：可修改 n 观察时间复杂度变化
    print(main(10))