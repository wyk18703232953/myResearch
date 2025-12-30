import random

def main(n):
    # 生成测试数据
    # 这里假设 k 在 [1, n] 之间随机生成，数组元素为 1~10^9 随机整数
    k = random.randint(1, n)
    arr = [random.randint(1, 10**9) for _ in range(n)]

    # 原逻辑开始
    bs = [[x, i + 1] for i, x in enumerate(arr)]
    bs.sort(reverse=True)
    cs = [bs[i][1] for i in range(k)]
    ans = sum(bs[i][0] for i in range(k))
    cs.sort()
    print(ans)
    if k == 1:
        print(n)
    else:
        print(cs[0], end=" ")
        for i in range(1, k - 1):
            print(cs[i] - cs[i - 1], end=" ")
        print(n - cs[k - 2])

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)