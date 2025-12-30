# Winners never quit, Quitters never win............................................................................
from collections import deque as de
import math
from collections import Counter as cnt
from functools import reduce
from typing import MutableMapping
from itertools import groupby as gb
from fractions import Fraction as fr
import random

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

class My_stack():
    def __init__(self):
        self.data = []
    def my_push(self, x):
        return (self.data.append(x))
    def my_pop(self):
        return (self.data.pop())
    def my_peak(self):
        return (self.data[-1])
    def my_contains(self, x):
        return (self.data.count(x))
    def my_show_all(self):
        return (self.data)
    def isEmpty(self):
      return len(self.data)==0

arrStack = My_stack()    

def decimalToBinary(n): 
    return bin(n).replace("0b", "")

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
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

def get_frequency(list_):
    dic={}
    for ele in list_:
        if ele in dic:
            dic[ele] += 1
        else:
            dic[ele] = 1
    return dic

def Log2(x): 
    return (math.log10(x) / math.log10(2))

def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

def ceildiv(x,y): 
    return (x+y-1)//y

# 生成测试数据并封装原逻辑
def main(n):
    """
    n: 用于控制规模的参数。
       我们生成两批数据，大小分别为 n 和 n（可以根据需要调整）。
       每条数据是一个 (key, value) 的整数对。
    """
    # 生成第一批 (a, x) 对
    first_pairs = []
    for _ in range(n):
        # key 和 value 的范围可根据需要调整
        a = random.randint(1, n * 2)
        x = random.randint(1, n * 10)
        first_pairs.append((a, x))

    # 生成第二批 (b, y) 对
    second_pairs = []
    for _ in range(n):
        b = random.randint(1, n * 2)
        y = random.randint(1, n * 10)
        second_pairs.append((b, y))

    # 原始逻辑开始
    ans = {}
    # 相当于第一段 while n:
    for a, x in first_pairs:
        ans[a] = x

    # 相当于第二段 while m:
    for b, y in second_pairs:
        if b in ans:
            if ans[b] < y:
                ans[b] = y
        else:
            ans[b] = y

    result = sum(list(ans.values()))
    print(result)
    return result

if __name__ == "__main__":
    # 示例：使用 n = 5 运行一次
    main(5)