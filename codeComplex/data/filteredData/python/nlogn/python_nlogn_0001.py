import random

def good(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    return x2 >= y1

def check(cent, n, t, x, a):
    for i in range(n):
        if not good(cent - t, cent + t, x[i] - a[i], x[i] + a[i]):
            return 0
    return 1

def main(n):
    # 生成测试数据
    # n: 区间个数
    # 生成 t, x[i], a[i]
    # 可按需调整范围
    t = random.randint(1, 10)
    x = [0] * n
    a = [0] * n
    for i in range(n):
        # 生成 x[i], a[i]
        xi = random.randint(-100, 100)
        ai = random.randint(0, 50)
        x[i] = xi * 2
        a[i] = ai

    ans = set()

    for i in range(n):
        val1 = x[i] - a[i] - t
        val2 = x[i] + a[i] + t
        if check(val1, n, t, x, a):
            ans.add(val1)
        if check(val2, n, t, x, a):
            ans.add(val2)

    print(len(ans))

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(5)