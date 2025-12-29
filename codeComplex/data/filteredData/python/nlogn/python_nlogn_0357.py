from random import randint


def solve(arr):
    for i in arr:
        for k in range(31):
            if i - (1 << k) in arr and i + (1 << k) in arr:
                return [i - (1 << k), i, i + (1 << k)]
    for i in arr:
        for k in range(31):
            if i + (1 << k) in arr:
                return [i, i + (1 << k)]
    for i in arr:
        return [i]


def main(n):
    # 根据规模 n 生成测试数据：
    # 生成 n 个不同的随机整数，范围可按需调整
    # 为了保持可读性，这里使用 1..10^9 的范围
    arr = set()
    while len(arr) < n:
        arr.add(randint(1, 10**9))

    lst = solve(arr)

    # 输出结果
    print(len(lst))
    for x in lst:
        print(x, end=' ')


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)