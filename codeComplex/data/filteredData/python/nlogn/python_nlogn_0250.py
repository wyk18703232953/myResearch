import random

def main(n):
    # 生成测试数据
    # n 为数组 a 的规模，同时我们也用它作为 q 的规模
    q = n

    # 生成 a：元素为 1~10 的正整数
    a = [random.randint(1, 10) for _ in range(n)]

    # 生成 k：元素为 1~10 的正整数
    k = [random.randint(1, 10) for _ in range(q)]

    # 前缀和数组
    pr_a = [0] * n
    for i in range(n):
        pr_a[i] = a[i] + (pr_a[i - 1] if i > 0 else 0)

    def p(c_k, r):
        l = 0
        while r - l > 1:
            z = (r + l) // 2
            if pr_a[z] > c_k:
                r = z
            else:
                l = z
        return l

    c_k = 0
    ans = []
    for qq in range(q):
        c_k += k[qq]
        l = p(c_k, n - 1)
        if pr_a[l] <= c_k:
            l += 1
        if c_k >= pr_a[n - 1]:
            c_k = 0
            l = 0
        ans.append(str(n - l))

    print("\n".join(ans))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)