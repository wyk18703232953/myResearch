# Mamma don't raises quitter.................................................
from collections import deque as de
import math
from collections import Counter as cnt
from functools import reduce
from itertools import groupby as gb
from bisect import bisect_left as bl, bisect_right as br
import random

def factors(n):
    return set(reduce(list.__add__,
                ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

class My_stack():
    def __init__(self):
        self.data = []
    def my_push(self, x):
        return self.data.append(x)
    def my_pop(self):
        return self.data.pop()
    def my_peak(self):
        return self.data[-1]
    def my_contains(self, x):
        return self.data.count(x)
    def my_show_all(self):
        return self.data
    def isEmpty(self):
        return len(self.data) == 0

arrStack = My_stack()

# decimal to binary
def decimalToBinary(n):
    return bin(n).replace("0b", "")

# binary to decimal
def binarytodecimal(n):
    return int(n, 2)

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

def get_prime_factors(number):
    prime_factors = []
    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i
    if number > 2:
        prime_factors.append(int(number))
    return prime_factors

def get_frequency(lst):
    dic = {}
    for ele in lst:
        if ele in dic:
            dic[ele] += 1
        else:
            dic[ele] = 1
    return dic

def Log2(x):
    return (math.log10(x) / math.log10(2))

# Function to get product of digits
def getProduct(n):
    product = 1
    while n != 0:
        product = product * (n % 10)
        n = n // 10
    return product

# function to find LCM of two numbers
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

# to check whether the given sorted sequence is forming an AP or not....
def checkisap(lst):
    d = lst[1] - lst[0]
    for i in range(2, len(lst)):
        temp = lst[i] - lst[i - 1]
        if temp != d:
            return False
    return True

# ceil  function gives wrong answer after 10^17 so i have to create my own :)
def ceildiv(x, y):
    return (x + y - 1) // y


def main(n):
    """
    n: 规模参数，用于控制测试数据生成范围。
       这里使用 n 作为最大位置索引，生成:
       1 <= pos <= n, 1 <= l <= r <= n
    """
    if n < 1:
        return

    # 根据 n 生成测试数据
    # n 固定为问题中的 n，pos, l, r 在 [1, n] 范围内随机生成，且保证 l <= r
    pos = random.randint(1, n)
    l = random.randint(1, n)
    r = random.randint(l, n)

    # 原始核心逻辑
    if l == 1 and r == n:
        print(0)
    else:
        if pos < l:
            ans = l - pos + 1
            if r < n:
                ans += (r - l)
                ans += 1
            print(ans)
        elif l <= pos <= r:
            if l > 1 and r < n:
                ans = (r - l)
                ans += min(pos - l, r - pos)
                ans += 2
            elif l > 1 and r == n:
                ans = pos - l
                ans += 1
            else:
                ans = r - pos
                ans += 1
            print(ans)
        else:
            ans = pos - r + 1
            if l > 1:
                ans += (r - l)
                ans += 1
            print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模自定
    main(10)