import random

def main(n):
    # 生成测试数据
    # 约定：k 在 [1, n] 内随机生成
    k = random.randint(1, n)
    # 生成一个非降序数组 a，保证原逻辑中 a[-1] - a[0] 有意义
    a = []
    cur = random.randint(-10, 10)
    for _ in range(n):
        cur += random.randint(0, 10)  # 保证非降序
        a.append(cur)

    # 原逻辑开始
    ans = a[-1] - a[0]
    delta = [-a[i] + a[i - 1] for i in range(1, n)]
    delta.sort()
    ans += sum(delta[:(k - 1)])
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)