import random

def main(n):
    # 生成测试数据
    # 约束：a[i]*10^11 不会超出常规整型范围即可，自由选择
    # 为了体现原算法含义，生成 1 <= a[i] < 10^11，k 取一个适中值
    k = random.randint(2, 10**9)
    a = [random.randint(1, 10**11) for _ in range(n)]

    # 原逻辑开始
    rda = []
    for j in range(12):
        rd = dict()
        x = pow(10, j)
        for i in range(n):
            r = (a[i] * x) % k
            rd[r] = rd.setdefault(r, 0) + 1
        rda.append(rd)

    ans = 0
    for i in range(n):
        r = a[i] % k
        ln = len(str(a[i]))
        x = pow(10, ln)
        if r == 0:
            r = k
        if k - r in rda[ln]:
            ans += rda[ln][k - r]
            if (a[i] * x) % k == k - r:
                ans -= 1

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 n=5
    main(5)