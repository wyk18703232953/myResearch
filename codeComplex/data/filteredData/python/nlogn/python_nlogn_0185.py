import random

def main(n):
    # 生成规模为 n 的测试数据，这里生成 [-10^6, 10^6] 范围内的随机整数
    arr = [random.randint(-10**6, 10**6) for _ in range(n)]

    mp = {}
    s = 0
    ans = 0
    i = 0

    for x in arr:
        i += 1
        s += x

        if x not in mp:
            mp[x] = 0
        if x + 1 not in mp:
            mp[x + 1] = 0
        if x - 1 not in mp:
            mp[x - 1] = 0

        mp[x] += 1

        adj = mp[x] + mp[x + 1] + mp[x - 1]

        c = s
        c -= mp[x] * x
        c -= mp[x + 1] * (x + 1)
        c -= mp[x - 1] * (x - 1)

        valid = i - adj
        ans += (valid * x) - c

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)