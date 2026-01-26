from collections import deque as de
import math
from collections import Counter as cnt
from functools import reduce
from typing import MutableMapping
from itertools import groupby as gb
from fractions import Fraction as fr

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
            math.log10(2))

def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

def ceildiv(x,y): 
    return (x+y-1)//y

def main(n):
    # Interpret n as total number of (key, value) pairs.
    # We split them deterministically into two groups:
    # first n//2 pairs for the first phase, remaining for the second phase.
    total_pairs = max(0, n)
    first_count = total_pairs // 2
    second_count = total_pairs - first_count

    # Generate deterministic (a, x) pairs for the first loop
    # and (b, y) pairs for the second loop.
    # Keys can repeat to exercise the update logic.
    ans = {}

    # First phase: simulate the original "n, then n lines: a x"
    for i in range(first_count):
        a = i  # deterministic key
        x = (i * 2) + 1  # deterministic value
        ans[a] = x

    # Second phase: simulate "m, then m lines: b y"
    # using the remaining pairs
    for j in range(second_count):
        # Shift keys to create overlaps and new keys
        b = j // 2
        y = (j * 3) + 2
        if b in ans:
            if ans[b] < y:
                ans[b] = y

        else:
            ans[b] = y

    result = sum(ans.values())
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)