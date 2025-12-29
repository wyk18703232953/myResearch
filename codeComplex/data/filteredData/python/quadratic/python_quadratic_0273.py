import sys
from collections import OrderedDict
from fractions import Fraction
import math

# decimal to binary
def binary(n):
    return bin(n).replace("0b", "")

# binary to decimal
def decimal(s):
    return int(s, 2)

# power of a number base 2
def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p

# if number is prime in √n time
def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

# list to string ,no spaces
def lts(l):
    return ''.join(map(str, l))

# string to list of characters
def stl(s):
    return list(s)

# Returns list of numbers with a particular sum
def sq(a, target, arr=None):
    if arr is None:
        arr = []
    s = sum(arr)
    if s == target:
        return arr
    if s >= target:
        return None
    for i in range(len(a)):
        n = a[i]
        remaining = a[i + 1:]
        ans = sq(remaining, target, arr + [n])
        if ans:
            return ans
    return None

mod = int(1e9) + 7

def main(n):
    # 生成测试数据：
    # 设 m = n，x 和 y 均为 [1, 2, ..., n]
    m = n
    x = list(range(1, n + 1))
    y = list(range(1, n + 1))

    # 原逻辑：输出 x 中也在 y 中的元素
    for c in x:
        if c in y:
            print(c, end=" ")

if __name__ == "__main__":
    # 示例：可以手动调用 main(5) 测试
    main(5)