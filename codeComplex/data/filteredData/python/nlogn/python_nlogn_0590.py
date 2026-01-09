from math import ceil

def main(n: int):
    d = {1: [1], 2: [1, 2], 3: [1, 1, 3]}

    def f(x):
        if x in d:
            return d[x][:]
        odds = ceil(x / 2)
        lis = [1] * odds
        even = x // 2
        lis1 = f(even)
        for i in range(len(lis1)):
            lis1[i] *= 2
        return lis + lis1

    if n in d:
        ans = d[n]

    else:
        ans = f(n)

    for v in ans:
        # print(v, end=' ')
        pass
if __name__ == "__main__":
    # 这里根据 n 生成测试数据，用户可自行修改 n 的值
    test_n = 10
    main(test_n)