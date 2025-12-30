import random

def main(n: int):
    # 1. 生成测试数据：长度为 n 的整数数组 a
    #   这里示例：生成 [0, 1, 2, ..., n-1] 再随机打乱
    a = list(range(n))
    random.shuffle(a)

    # 原逻辑开始
    a = sorted(a)

    ans = [0] * n
    ans[0] = 1
    f = ans[0] != a[0]
    for i in range(1, n):
        ans[i] = a[i - 1]
        if ans[i] != a[i]:
            f = True

    m = 10**9
    if not f:
        for i in range(n - 1, -1, -1):
            if ans[i] < m:
                ans[i] += 1
                break

    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)