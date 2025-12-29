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

def decimalToBinary(n): 
    return bin(n).replace("0b", "")

def isPrime(n): 
    if n <= 1:
        return False
    if n <= 3:
        return True
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
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
    return math.log10(x) / math.log10(2)

def isPowerOfTwo(n): 
    return math.ceil(Log2(n)) == math.floor(Log2(n))

def main(n):
    # 根据规模 n 生成测试数据：
    # n 行，每行长度 m，m 与 n 同阶，这里设 m = max(1, n)
    m = max(1, n)

    # 构造一个 n x m 的 0/1 矩阵，元素为整数 0 或 1
    l = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]

    dic = {}
    discarded = {}

    for i in range(n):
        for j in range(m):
            if l[i][j] == 1:
                if j + 1 not in discarded:
                    if j + 1 not in dic:
                        dic[j + 1] = i + 1
                    else:
                        del dic[j + 1]
                        discarded[j + 1] = 1

    if len(dic) == 0:
        print("YES")
    else:
        kk = list(dic.values())
        temp = list(set(kk))
        if len(temp) == n:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)