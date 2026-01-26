def main(n):
    # 映射：n 是题目中的原始 n（元素个数）
    # 为了可扩展实验，这里生成确定性数据：
    # l, r, x 以及数组 c 都由 n 确定性构造
    if n <= 0:
        return 0

    # 确定性构造参数
    l = n * (n + 1) // 4          # 大约是 sum(range(1,n+1))/2 的一半量级
    r = n * (n + 1) // 2          # sum(range(1,n+1))，保证上界足够大
    x = max(1, n // 4)            # 随 n 增长的差值要求

    # 确定性构造数组 c，保持“难度”随 n 线性增长
    c = [i + 1 for i in range(n)]

    ans = 0
    # 原逻辑：枚举所有非空子集
    for mask in range(1, 1 << n):
        v = []
        for j in range(n):
            if mask & (1 << j):
                v.append(c[j])
        s = sum(v)
        if l <= s <= r and max(v) - min(v) >= x:
            ans += 1
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 用于时间复杂度实验
    main(10)