import random

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def ncr(n, r):
    from functools import reduce
    import operator as op
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom

def main(n):
    # 根据规模 n 生成测试数据：生成 n 个随机整数
    # 为了尽量能产生三等差数列，用较小范围
    max_val = max(3 * n, 10)
    arr = [random.randint(0, max_val) for _ in range(n)]

    sett = set(arr)
    ans = [arr[0]]
    flag = 0

    for x in range(31):
        step = 2 ** x
        for i in arr:
            if (i - step) in sett and (i + step) in sett:
                ans = [i - step, i, i + step]
                flag = 1
                break
            elif (i - step) in sett:
                ans = [i - step, i]
            elif (i + step) in sett:
                ans = [i, i + step]
        if flag:
            break

    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    # 示例：调用 main，规模可自行调整
    main(10)