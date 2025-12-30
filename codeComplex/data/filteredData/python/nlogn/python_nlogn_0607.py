import random

mod = 1000000007

def main(n):
    # 生成测试数据
    # 约定：k <= n，a 中元素为 [1, 10^9] 内的随机整数
    k = max(1, n // 2)  # 示例生成：令 k 为 n 的一半（至少为 1）
    a = [random.randint(1, 10**9) for _ in range(n)]

    # 原逻辑开始
    a.sort()

    ans = 0
    c = 1

    for i in range(n):
        if c > a[n - 1] or c > a[i]:
            ans += a[i] - 1
            continue
        if i != n - 1:
            ans += a[i] - 1
            c += 1
        else:
            ans += c - 1

    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)