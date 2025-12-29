import random

def main(n):
    # 生成测试数据
    # 约定：a 中元素为 1~10^9 的随机整数，k 为 1~10^9 的随机正整数
    # 如有需要可在此处修改数据生成策略
    if n <= 0:
        print(0)
        return

    # 避免 k 为 0
    k = random.randint(1, 10**9)
    a = [random.randint(1, 10**9) for _ in range(n)]

    # 原逻辑开始
    b = []
    for i in range(11):
        c = {}
        for j in range(n):
            d = (a[j] * (10**i)) % k
            if d in c:
                c[d] += 1
            else:
                c[d] = 1
        b.append(c)

    s = 0
    for i in range(n):
        cmod = a[i] % k
        d = (k - cmod) % k
        length = len(str(a[i]))
        if d in b[length]:
            s += b[length][d]
        if (a[i] * (10**length)) % k == d:
            s -= 1

    print(s)


# 示例：调用 main(5) 进行一次测试
if __name__ == "__main__":
    main(5)