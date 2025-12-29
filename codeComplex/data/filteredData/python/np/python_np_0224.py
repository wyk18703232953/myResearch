import random

def find(a, b):
    cc = 2
    for i in range(1, (1 << len(a))):
        sx = 0
        minn = 100000000
        maxn = -1
        for j in range(len(a)):
            if i & (1 << j):
                sx += a[j]
                minn = min(minn, a[j])
                maxn = max(maxn, a[j])
        if sx >= b[1] and sx <= b[2] and (maxn - minn) >= b[3]:
            cc += 1
    if cc < 2:
        return 2
    else:
        return cc - 2

def main(n: int):
    """
    n: 规模，用作数组 a 的长度
    自动生成测试数据：
      - b[1], b[2] 为和的区间
      - b[3] 为最大值与最小值之差的下限
    """
    # 生成数组 a，元素范围可以根据需要调整
    a = [random.randint(1, 20) for _ in range(n)]

    # 生成 b：
    # b[0] 原代码未使用，这里保留为 0
    # b[1], b[2]: 和区间
    # b[3]: max - min 下限
    total_min = min(a)
    total_max = max(a)
    sum_a = sum(a)

    # 合理构造区间 [L, R]
    L = random.randint(total_min, max(total_min, sum_a // 2))
    R = random.randint(L, sum_a)

    diff_lower_bound = random.randint(0, max(0, total_max - total_min))

    b = [0, L, R, diff_lower_bound]

    result = find(a, b)
    print("a:", a)
    print("b:", b)
    print("result:", result)
    return result

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)