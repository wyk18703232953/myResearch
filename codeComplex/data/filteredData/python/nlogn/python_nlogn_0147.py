import random

def main(n):
    # 生成测试数据
    # 生成一个随机的 k (>=2，避免除以1无意义的情况)
    k = random.randint(2, 10)

    # 生成长度为 n 的数组 a，每个元素在 [1, 10*n] 之间
    a = [random.randint(1, 10 * n) for _ in range(n)]

    # 原逻辑开始
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1  # 原代码为1，等价于出现次数不影响逻辑，可用计数更稳健

    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        if d.get(a[i], 0) > 0:
            if a[i] % k == 0:
                x = a[i] // k
                if x in d:
                    d[x] -= 1
            d[a[i]] -= 1  # 补上自身使用一次
            ans += 1

    print("n =", n)
    print("k =", k)
    print("a =", a)
    print("ans =", ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)