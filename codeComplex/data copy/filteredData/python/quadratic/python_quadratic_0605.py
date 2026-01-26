def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def core_algorithm(n, m, k, a):
    ans = 0
    for i in range(m):
        li = a[0:i] + [-k]
        s = 0
        while True:
            li += a[i+s:min(i+m+s, len(a))]
            li += [-k]
            if i+m+s >= len(a):
                break
            s += m
        ans = max(max_subarray(li) - k, ans)
    return ans

def generate_input(n):
    # 映射含义：
    # n: 数组长度，同时线性控制 m 和 k 的规模
    if n <= 0:
        n = 1
    length = n
    # 生成 a: 既有正数也有负数，确定性构造
    # a[i] = ((i % 7) - 3) * ((i % 5) + 1)
    a = [((i % 7) - 3) * ((i % 5) + 1) for i in range(length)]
    # 生成 m: 子段步长，保证 1 <= m <= n
    m = max(1, n // 3)
    if m > n:
        m = n
    # 生成 k: 惩罚值，随 n 线性增长，且为正
    k = n // 2 + 1
    return n, m, k, a

def main(n):
    n, m, k, a = generate_input(n)
    result = core_algorithm(n, m, k, a)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)