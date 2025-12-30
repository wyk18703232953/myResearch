from random import randint


def main(n):
    # 1. 生成测试数据：长度为 n 的数组 a，元素在一个合理范围内
    # 为了更容易出现有意义的答案，这里选取范围 [-10^6, 10^6]
    a = [randint(-10**6, 10**6) for _ in range(n)]

    # 2. 原逻辑开始
    d = {}
    power = [2 ** i for i in range(31)]
    ans = []

    for i in a:
        d[i] = 0

    for num in d.keys():
        for p in power:
            if num + p in d:
                ans = [num, num + p]
                if num + p + p in d:
                    print(3)
                    ans.append(num + p + p)
                    print(*ans)
                    return
    if ans:
        print(2)
        print(*ans)
    else:
        print(1)
        print(a[0])


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)