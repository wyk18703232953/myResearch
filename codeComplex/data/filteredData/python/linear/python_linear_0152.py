from collections import deque as de
import math
import re
from collections import Counter as cnt
from functools import reduce
from typing import MutableMapping
from itertools import groupby as gb
from fractions import Fraction as fr
from bisect import bisect_left as bl, bisect_right as br
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

#decimal to binary   
def decimalToBinary(n): 
    return bin(n).replace("0b", "")
#binary to decimal
def binarytodecimal(n):
    return int(n,2)

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

def get_frequency(list):
    dic={}
    for ele in list:
        if ele in dic:
            dic[ele] += 1
        else:
            dic[ele] = 1
    return dic

def Log2(x): 
    return (math.log10(x) / math.log10(2)); 

# Function to get product of digits
def getProduct(n):
    product = 1
    while (n != 0):
        product = product * (n % 10)
        n = n // 10
    return product

# function to count consecutive duplicate element in an array
def dupconscount(nums):
    element = []
    freque = []
    if not nums:
        return element
    running_count = 1
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            running_count += 1
        else:
            freque.append(running_count)
            element.append(nums[i])
            running_count = 1
    freque.append(running_count)
    element.append(nums[i+1])
    return element,freque

def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n))); 

#ceil  function gives wrong answer after 10^17 so i have to create my own :)
def ceildiv(x,y): 
    return (x+y-1)//y 

def main(n):
    # 生成测试数据：
    # n: 数组长度
    # p: 模数，至少为 1，简单起见设为一个较大的值
    p = max(1, n * 10 + 7)
    # 生成数组 a，元素为 0..p-1 之间的随机数
    random.seed(0)
    a = [random.randint(0, p - 1) for _ in range(n)]

    # 原逻辑开始
    fir = a[0]
    sec = sum(a) - fir
    ans = (fir % p) + (sec % p)
    for i in range(1, n):
        fir += a[i]
        sec -= a[i]
        temp = (fir % p) + (sec % p)
        if temp > ans:
            ans = temp

    print(ans)

if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(5)