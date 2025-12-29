import random

def main(n):
    # 生成测试数据
    # a: n 个 1~10 的随机整数
    # b: 由 'W', 'G', 'L' 组成的长度为 n 的随机字符串
    a = [random.randint(1, 10) for _ in range(n)]
    b = ''.join(random.choice('WGL') for _ in range(n))

    sol = 0
    e = 0
    big = 0
    g = 0
    for i in range(n):
        if b[i] == "W":
            big = 1
            sol += 3 * a[i]
            e += a[i]
        if b[i] == "G":
            sol += 5 * a[i]
            e += a[i]
            g += 2 * a[i]
        if b[i] == "L":
            sol += a[i]
            e -= a[i]
            if e < 0:
                if big:
                    sol -= 3 * e
                else:
                    sol -= 5 * e
                e = 0
        g = min(e, g)
    if e:
        sol -= 2 * g
        sol -= (e - g)
    print(int(sol))


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)