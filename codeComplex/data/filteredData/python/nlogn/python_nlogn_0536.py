import random

def main(n):
    # 生成测试数据：n 个随机整数和一个随机 k
    # 你可以根据需要调整数据范围
    k = random.randint(1, 10**9)
    a = [random.randint(1, 10**9) for _ in range(n)]

    bank = {}

    # Preparation
    for i in range(n):
        arg = (len(str(a[i])), a[i] % k)
        bank[arg] = bank.get(arg, 0) + 1

    ans = 0
    # Query
    for i in range(n):
        ten = 1
        for j in range(1, 11):
            ten *= 10
            frontMod = (a[i] * ten) % k
            req = (k - frontMod) % k
            got = bank.get((j, req), 0)
            ans += got

    # Deal with Same Index
    for i in range(n):
        cur = str(a[i])
        cur2 = cur * 2
        tst = int(cur2)
        if tst % k == 0:
            ans -= 1

    print(ans)


if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)