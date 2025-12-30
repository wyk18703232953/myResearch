import random

def main(n):
    # 生成测试数据
    # 约束范围可按需要调整
    l = random.randint(1, 50)
    r = random.randint(l, l + 100)  # 保证 r >= l
    x = random.randint(0, 50)

    # 生成数组 arr，元素为正整数
    arr = [random.randint(1, 50) for _ in range(n)]

    ans = 0
    for mask in range(1 << n):
        subset = []
        for j in range(n):
            if (mask & (1 << j)) != 0:
                subset.append(arr[j])
        if len(subset) > 1:
            mx = max(subset)
            mn = min(subset)
            sm = sum(subset)
            if l <= sm <= r and mx - mn >= x:
                ans += 1

    print(ans)

if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)