def main(n):
    # 映射：n 作为数组长度，m 为 n//2
    if n <= 0:
        return 0
    m = n // 2 if n // 2 > 0 else 1
    # 生成确定性数据：
    # c: 严格递增序列，从 1 开始
    # a: 从 2 开始的递增序列，保证部分匹配
    c = [i + 1 for i in range(n)]
    a = [2 * (i + 1) for i in range(m)]
    j, res = 0, 0
    for i in range(n):
        if j < m:
            if c[i] <= a[j]:
                j += 1
                res += 1
    return res

if __name__ == "__main__":
    # 示例调用
    print(main(10))