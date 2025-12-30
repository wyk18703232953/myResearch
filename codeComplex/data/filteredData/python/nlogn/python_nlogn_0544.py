import random

def main(n):
    # 生成测试数据：随机生成 k 和 n 个数
    # 约束条件可根据需要调整
    k = random.randint(1, 10**9)
    # 避免 k = 0 的情况（上面已保证 >=1）
    a = [str(random.randint(1, 10**9)) for _ in range(n)]

    mods = [dict() for _ in range(10)]
    l = [0] * n

    for i in range(n):
        l[i] = len(a[i])
        a[i] = int(a[i]) % k
        cur = a[i]
        for j in range(10):
            cur = cur * 10 % k
            mods[j][cur] = mods[j].get(cur, 0) + 1

    ans = 0
    for i in range(n):
        mod = (k - a[i]) % k
        ans += mods[l[i] - 1].get(mod, 0)
        cur = a[i]
        for _ in range(l[i]):
            cur = cur * 10 % k
        if cur == mod:
            ans -= 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，n 为规模
    main(5)