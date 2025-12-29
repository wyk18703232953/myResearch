import random

def main(n):
    # 生成测试数据：
    # 随机生成 n 个整数，并随机选一个位置作为 m 的值
    a = [random.randint(0, 10) for _ in range(n)]
    aim = random.randrange(n)
    m = a[aim]

    diff = [0] * n
    for i in range(n):
        if a[i] < m:
            diff[i] = -1
        elif a[i] > m:
            diff[i] = 1

    # 若 m 在 a 中不止一次，保持和原程序逻辑一致：使用第一次出现的位置
    aim = a.index(m)

    left = {}
    right = {}
    suml = 0
    for i in reversed(range(aim + 1)):
        suml += diff[i]
        if suml not in left:
            left[suml] = 0
        left[suml] += 1

    sumr = 0
    for i in range(aim, n):
        sumr += diff[i]
        if sumr not in right:
            right[sumr] = 0
        right[sumr] += 1

    ans = 0
    for s in left:
        wk1 = -s
        if wk1 in right:
            ans += left[s] * right[wk1]
        wk1 = 1 - s
        if wk1 in right:
            ans += left[s] * right[wk1]

    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)