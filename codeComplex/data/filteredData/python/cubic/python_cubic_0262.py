import random

rr = 0
gg = 0
bb = 0
dp = []


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def power(x, p, m):
    res = 1
    while p:
        if p & 1:
            res = (res * x) % m
        x = (x * x) % m
        p >>= 1
    return res


def lcm(num1, num2):
    return (num1 * num2) // gcd(num1, num2)


def func(x, y, z, red, green, blue):
    if (x >= rr and y >= gg) or (y >= gg and z >= bb) or (x >= rr and z >= bb):
        return 0
    if dp[x][y][z] != -1:
        return dp[x][y][z]
    take = 0
    if x < rr and y < gg:
        take = max(take, red[x] * green[y] + func(x + 1, y + 1, z, red, green, blue))
    if y < gg and z < bb:
        take = max(take, green[y] * blue[z] + func(x, y + 1, z + 1, red, green, blue))
    if x < rr and z < bb:
        take = max(take, red[x] * blue[z] + func(x + 1, y, z + 1, red, green, blue))
    dp[x][y][z] = take
    return take


def main(n):
    """
    n: 控制规模的参数，表示 rr, gg, bb 的最大长度。
       实际上三种颜色的长度分别随机设为 1..n 之间的值。
    返回：原程序应输出的最大得分值。
    """
    global rr, gg, bb, dp

    # 随机生成 rr, gg, bb，范围 1..n
    rr = random.randint(1, n)
    gg = random.randint(1, n)
    bb = random.randint(1, n)

    # 随机生成三个数组的值（正整数），范围 1..100
    red = [random.randint(1, 100) for _ in range(rr)]
    green = [random.randint(1, 100) for _ in range(gg)]
    blue = [random.randint(1, 100) for _ in range(bb)]

    red.sort(reverse=True)
    green.sort(reverse=True)
    blue.sort(reverse=True)

    # 初始化 dp，维度 (rr+1) x (gg+1) x (bb+1)，全部为 -1
    dp.clear()
    for _ in range(rr + 1):
        temp = []
        for _ in range(gg + 1):
            lis = [-1] * (bb + 1)
            temp.append(lis)
        dp.append(temp)

    ans = func(0, 0, 0, red, green, blue)
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：以 n = 5 运行一次
    main(5)