import random

def solve(n, k):
    upper_bound = n + 1
    lower_bound = -1
    while upper_bound > lower_bound + 1:
        m = (upper_bound + lower_bound) // 2
        if (n - m) * (n - m + 1) // 2 - m > k:
            lower_bound = m
        else:
            upper_bound = m
    return upper_bound

def main(n):
    # 根据 n 生成测试数据：
    # 原题中 k 的量级取决于 n，(n-m)(n-m+1)/2 大致为 O(n^2)，
    # 因此这里随机生成一个 0 到 n*(n+1)//2 范围内的 k。
    k = random.randint(0, n * (n + 1) // 2)
    ans = solve(n, k)
    print(ans)

if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(10)