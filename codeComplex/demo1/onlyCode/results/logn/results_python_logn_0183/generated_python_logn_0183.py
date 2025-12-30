import random

def main(n):
    # 根据 n 生成测试数据，这里生成 s 为 [0, n] 区间内的随机整数
    s = random.randint(0, n)

    def check(x):
        y = list(str(x))
        ans = x
        for i in y:
            ans -= int(i)
        return ans >= s

    ans = 0
    l = 1
    r = n
    while l <= r:
        m = (l + r) // 2
        if check(m):
            ans = n - m + 1
            r = m - 1
        else:
            l = m + 1

    print(ans)

# 示例：调用 main(10**6) 等
# main(1000)