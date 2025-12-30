import random

def main(n):
    # 生成测试数据
    # p: 取一个合理范围的正整数
    p = random.randint(1, 10 * n + 1)
    # arr: 生成 n 个非负整数
    arr = [random.randint(0, 10**6) for _ in range(n)]

    # 原逻辑开始
    su = 0
    for i in range(n):
        su += arr[i]
    maxi, f = 0, 0
    for i in range(n - 1):
        f += arr[i]
        maxi = max(maxi, f % p + (su - f) % p)
    print(maxi)

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)