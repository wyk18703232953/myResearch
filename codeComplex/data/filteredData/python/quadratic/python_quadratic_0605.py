import random

def max_subarray(A):
    # Kadane 算法
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def main(n):
    """
    n: 规模参数，用来生成测试数据
    这里约定：
      - 数组长度 len(a) = n
      - m 在 [1, n] 内随机
      - k 在 [1, 10] 内随机
      - a 中元素在 [-10, 10] 内随机
    """
    if n <= 0:
        return 0

    # 生成测试数据
    length = n
    a = [random.randint(-10, 10) for _ in range(length)]
    m = random.randint(1, length)
    k = random.randint(1, 10)

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
    return ans