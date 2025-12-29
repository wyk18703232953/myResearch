import random

def main(n):
    # 生成测试数据
    # 随机选择 k >= 2
    k = random.randint(2, 10)
    # 生成 n 个正整数
    arr = [random.randint(1, 10 * n + 10) for _ in range(n)]

    # 原逻辑开始
    if k == 1:
        print(n)
        return

    a = sorted(arr)
    a = dict(zip(a, range(n)))  # 实际上只取 key 集合

    b = {}
    count = {}

    for x in a.keys():
        if x % k == 0 and int(x / k) in a:
            b[x] = b[int(x / k)]
            count[b[int(x / k)]] += 1
        else:
            b[x] = x
            count[x] = 1

    ans = n
    for _, y in count.items():
        ans -= int(y / 2)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)