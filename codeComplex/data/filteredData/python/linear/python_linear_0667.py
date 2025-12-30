import random

def main(n):
    # 生成测试数据
    # n: 序列长度
    # a: 长度为 n 的正整数数组
    # b: 长度为 n 的字符串，仅包含 'W', 'G', 'L'
    a = [random.randint(1, 10) for _ in range(n)]
    choices = ['W', 'G', 'L']
    b = ''.join(random.choice(choices) for _ in range(n))

    # 求解逻辑
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
        g = min(g, e)
    if e:
        sol -= 2 * g
        sol -= (e - g)
    return int(sol)


if __name__ == "__main__":
    # 示例：规模为 10
    result = main(10)
    print(result)