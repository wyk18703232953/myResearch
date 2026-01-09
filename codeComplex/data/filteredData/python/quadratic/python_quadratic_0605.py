def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def main(n):
    # 映射规则：
    # n >= 3，用作数组长度；m 和 k 与 n 相关以保证可规模化
    if n < 3:
        n = 3

    # 构造 n, m, k
    length = n
    m = max(1, n // 3)      # 步长规模随 n 线性增长
    k = max(1, n // 5)      # 惩罚值随 n 线性增长

    # 构造数组 a，长度为 length，包含正负数，完全确定性
    # 示例：a[i] = (i % 7) - 3
    a = [(i % 7) - 3 for i in range(length)]

    ans = 0
    for i in range(m):
        li = a[0:i] + [-k]
        s = 0
        while True:
            li += a[i + s:min(i + m + s, len(a))]
            li += [-k]
            if i + m + s >= len(a):
                break
            s += m
        ans = max(max_subarray(li) - k, ans)
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)