import random

def main(n: int):
    # 生成测试数据：
    # 1. 生成一个从 1..n 的随机排列作为置换 a
    # 2. 为每个位置生成一个正权值 c[i]
    # 为了与原代码结构一致，a 和 c 都从下标 1 开始，0 号位填充占位符。
    a = [0] + random.sample(range(1, n + 1), n)
    c = [0] + [random.randint(1, 10**6) for _ in range(n)]

    vis = [0] * (n + 1)
    ans = 0
    for i in range(1, n + 1):
        x = i
        while vis[x] == 0:
            vis[x] = i
            x = a[x]
        if vis[x] != i:
            continue
        v = x
        mn = c[x]
        while a[x] != v:
            x = a[x]
            mn = min(mn, c[x])
        ans += mn
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)