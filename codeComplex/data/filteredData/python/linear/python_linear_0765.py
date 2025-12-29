import collections
import random
import math
from sys import stdout

mod = (10 ** 9) + 7

def modinv(n, p):
    return pow(n, p - 2, p)

def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def isprime(x):
    if x == 1:
        return False
    elif x < 4:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def main(n):
    # 生成测试数据：
    # n 为数组规模，q 为查询数量（这里设置为 n）
    q = n

    # 生成一个随机排列，使最大值出现在随机位置
    a = list(range(1, n + 1))
    random.shuffle(a)

    # 生成随机查询（使用 1 到 2*n 之间的随机数，覆盖前期与周期后期）
    queries = [random.randint(1, 2 * n) for _ in range(q)]

    # 以下为原逻辑的无 input() 改写
    g = max(a)
    d = collections.deque(a)
    f = 0
    an1 = []

    # 模拟直到最大值到最前面并固定
    while d[0] != g:
        f += 1
        x = d.popleft()
        y = d.popleft()
        an1.append(str(x) + " " + str(y))
        if y == g:
            d.appendleft(y)
            d.append(x)
            break
        if x < y:
            d.appendleft(y)
            d.append(x)
        else:
            d.appendleft(x)
            d.append(y)

    r = []
    ans = []
    for _ in range(n):
        r.append(str(d.popleft()))

    for b in queries:
        if b <= f:
            ans.append(an1[b - 1])
        else:
            b -= f
            b -= 1
            b %= (n - 1)
            ans.append(r[0] + " " + r[b + 1])

    stdout.write("\n".join(ans))


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)