import random

def main(n):
    # n 为规模，这里解释为数组长度
    # 生成测试数据：
    # n_list: [dummy0, dummy1, k]，其中 dummy1 = n，k 随机生成
    # a: 长度为 n 的整数数组，严格递增，模拟原逻辑常见输入形式
    if n <= 0:
        return 0

    k = random.randint(1, max(1, n // 2))  # 分组尺度
    a = []
    cur = random.randint(1, 5)
    for _ in range(n):
        a.append(cur)
        cur += random.randint(1, 5)

    n_list = [0, n, k]

    # 原逻辑开始
    k = n_list[2]
    ans = 0
    dele = 1
    i = 0
    while i < n_list[1]:
        count = 1
        while (i + count < n_list[1]) and ((a[i + count] - dele) // k == (a[i] - dele) // k):
            count += 1
        ans += 1
        dele += count
        i += count

    print(ans)
    return ans

if __name__ == "__main__":
    # 举例运行
    main(10)