import random

def main(n):
    # 生成测试数据
    # 随机选择 k >= 2
    k = random.randint(2, max(2, n))
    # 生成 n 个随机正整数，范围适当放大以增加可整除关系
    arr = [random.randint(1, 10 * n) for _ in range(n)]

    # 原逻辑开始
    if k == 1:
        print(n)
        return

    a = arr[:]
    a.sort()

    a = dict(zip(a, range(n)))
    b = {}
    count = {}

    for x in a:
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


# 示例调用
if __name__ == "__main__":
    main(10)