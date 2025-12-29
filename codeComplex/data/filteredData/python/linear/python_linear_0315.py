from random import randint

def main(n):
    # 随机生成 m（1 <= m <= n，且尽量避免 0 的极端情况）
    if n <= 0:
        return
    m = randint(1, max(1, n))

    # 生成测试数组 arr，元素范围可自行调节
    # 这里设置为 0 ~ 10^9
    arr = [randint(0, 10**9) for _ in range(n)]

    # 原逻辑开始
    s = sum(arr)
    x = [[] for _ in range(m)]
    for i in range(n):
        x[arr[i] % m].append(i)

    j = 0
    for i in range(m):
        while len(x[i]) > n // m:
            while j < i or len(x[j % m]) >= n // m:
                j += 1
            k = x[i].pop()
            arr[k] += (j - i) % m
            x[j % m].append(k)

    print(sum(arr) - s)
    print(*arr)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)