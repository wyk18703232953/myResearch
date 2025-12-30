from collections import deque as de
import math
from collections import Counter as cnt
from functools import reduce
from typing import MutableMapping
import random

def factors(n):    
    return set(reduce(list.__add__,
                ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))

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

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6
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
    return math.log10(x) / math.log10(2)

def isPowerOfTwo(n):
    return math.ceil(Log2(n)) == math.floor(Log2(n))

def main(n):
    # 生成测试数据
    # 设定 d 为 1 到 10 之间的随机整数
    d = random.randint(1, 10)
    # 生成严格递增的数组 x，长度为 n
    # 从 0 开始，每次加 1 到 5 的随机步长
    x = [0]
    for _ in range(1, n):
        x.append(x[-1] + random.randint(1, 5))

    # 原逻辑
    ans = 0
    for i in range(1, n):
        diff = x[i] - x[i - 1]
        if diff >= 2 * d:
            ans += min(2, (x[i] - d) - (x[i - 1] + d) + 1)
    ans += 2
    print(ans)

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)