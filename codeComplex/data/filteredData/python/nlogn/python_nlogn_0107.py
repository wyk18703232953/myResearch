import random

def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y >>= 1
        x = (x * x) % p
    return res

def prefix_sum(arr):
    r = [0] * (len(arr) + 1)
    for i, el in enumerate(arr):
        r[i + 1] = r[i] + el
    return r

def divideCeil(n, x):
    if n % x == 0:
        return n // x
    return n // x + 1

def main(n):
    # 生成测试数据：长度为 n 的整数数组
    # 这里生成 1 到 10^9 之间的随机整数
    l = [random.randint(1, 10**9) for _ in range(n)]

    l1 = l[:]
    l1.sort()
    pos = []
    for i in range(n):
        if l1[i] != l[i]:
            pos.append(i)

    if (len(pos) == 0) or (len(pos) == 2 and l[pos[0]] == l1[pos[1]] and l[pos[1]] == l1[pos[0]]):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需调整
    main(10)