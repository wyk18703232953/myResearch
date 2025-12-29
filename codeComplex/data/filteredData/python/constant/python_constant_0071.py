import sys
import math
from collections import deque, defaultdict
import operator as op
from functools import reduce
import random

def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def valid(row, col, rows, cols, rcross, lcross):
    return rows[row] == 0 and cols[col] == 0 and rcross[col + row] == 0 and lcross[col - row] == 0

def div(n):
    tmp = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n = n // i
                cnt += 1
            tmp.append((i, cnt))
    if n > 1:
        tmp.append((n, 1))
    return tmp

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

def s(b):
    ans = []
    while b > 0:
        tmp = b % 10
        ans.append(tmp)
        b = b // 10
    return ans

def main(n):
    # 使用 n 作为规模参数生成测试数据
    # 为保持原逻辑输出格式：print(n, 0, 0)
    # 这里假设 n 本身就是测试规模（可从中派生其他测试数据）
    # 示例：生成一个长度为 n 的随机数组（实际不参与输出，仅示例性使用）
    random.seed(0)
    test_array = [random.randint(1, 10**6) for _ in range(n)]
    # 可以在此调用上面定义的算法函数对 test_array 做任意处理

    print(n, 0, 0)

if __name__ == '__main__':
    # 示例：当直接运行脚本时，使用一个默认规模
    main(10)