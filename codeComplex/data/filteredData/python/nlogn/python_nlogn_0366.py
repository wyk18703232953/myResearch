from collections import deque as de
import math
from collections import Counter as cnt
from functools import reduce
from typing import MutableMapping

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
    return (math.log10(x) / 
            math.log10(2)); 

def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n))); 

def core_logic(n, k, a):
    dic = get_frequency(a)
    ss = sorted(list(set(a)))
    tobesubtracttion = 0
    for i in range(len(ss)-1):
        if ss[i+1] <= ss[i] + k:
            tobesubtracttion += dic[ss[i]]
    return n - tobesubtracttion

def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    k = max(1, n // 3)
    a = [(i * 2 + (i // 3)) % (2 * n + 1) for i in range(n)]
    result = core_logic(n, k, a)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)