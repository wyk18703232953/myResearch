import random

def main(n):
    # 随机生成参数 l, r, x 和数组 a
    # 为保证有解，先生成题目数组 a
    a = [random.randint(1, 10**6) for _ in range(n)]
    a_sorted = sorted(a)
    
    # 生成 l, r, x：
    #   sum(a) 为最大可能和，最小和为 min(a)
    total_sum = sum(a)
    min_a = min(a)
    max_a = max(a)
    
    # 生成 x：至少 1，至多 max_a - min_a
    if max_a > min_a:
        x = random.randint(1, max_a - min_a)
    else:
        x = 0  # 所有元素相同的极端情况，仅为完整性
    
    # 生成区间 [l, r]，在 [min_a, total_sum] 范围内
    l = random.randint(min_a, total_sum)
    r = random.randint(l, total_sum)
    
    cnt = 0
    for mask in range(0, 1 << n):
        s = 0
        mn = 10**18
        mx = 0
        for j in range(n):
            if (mask >> j) & 1:
                val = a[j]
                s += val
                if val < mn:
                    mn = val
                if val > mx:
                    mx = val
        if s >= l and s <= r and mx - mn >= x:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)