import random

def main(n):
    # 生成测试数据
    # n 为数组 a 的长度，同时也设 q = n
    q = n
    # a 中元素为 1~10 的随机正整数
    a = [random.randint(1, 10) for _ in range(n)]
    # k 中元素为 1~10 的随机正整数
    k = [random.randint(1, 10) for _ in range(q)]

    def p(c_k, r, pr_a):
        l = 0
        while r - l > 1:
            z = (r + l) // 2
            if pr_a[z] > c_k:
                r = z
            else:
                l = z
        return l

    # 构建前缀和数组 pr_a
    pr_a = [0] * n
    for i in range(n):
        pr_a[i] = a[i]
        if i > 0:
            pr_a[i] += pr_a[i - 1]

    c_k = 0
    ans = []
    for qq in range(q):
        c_k += k[qq]
        l = p(c_k, n - 1, pr_a)
        if pr_a[l] <= c_k:
            l += 1
        if c_k >= pr_a[n - 1]:
            c_k = 0
            l = 0
        ans.append(str(n - l))

    print('\n'.join(ans))


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)