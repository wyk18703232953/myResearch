from collections import deque as de
import math
from collections import Counter as cnt
from functools import reduce
from typing import MutableMapping
import random

def factors(n):    
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

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
    return math.log10(x) / math.log10(2)

def isPowerOfTwo(n):
    return math.ceil(Log2(n)) == math.floor(Log2(n))


def main(n: int):
    # 生成测试数据：
    # 1. 生成长度为 n 的括号串，保证有一定数量的括号对
    # 2. 生成 k 为不超过可匹配总括号数的最大偶数
    s = []
    balance = 0
    for _ in range(n):
        if balance == 0:
            # 只能放 '('
            s.append('(')
            balance += 1
        else:
            # 随机放 '(' 或 ')'
            if random.random() < 0.5:
                s.append('(')
                balance += 1
            else:
                s.append(')')
                balance -= 1
    # 计算最多可能匹配的括号对数量
    stack_tmp = 0
    pairs = 0
    for ch in s:
        if ch == '(':
            stack_tmp += 1
        else:
            if stack_tmp > 0:
                stack_tmp -= 1
                pairs += 1
    max_k = 2 * pairs
    if max_k == 0:
        k = 0
    else:
        # 在 [2, max_k] 内随机生成一个偶数 k
        candidate = random.randint(1, max_k // 2) * 2
        k = candidate

    # 按原逻辑处理
    global arrStack
    arrStack = My_stack()
    dic = {}
    for i in range(n):
        if s[i] == "(":
            arrStack.my_push([i, "("])
        else:
            if not arrStack.isEmpty() and arrStack.my_peak()[1] == "(":
                index = arrStack.my_peak()[0]
                dic[index] = 1
                dic[i] = 1
                k -= 2
                arrStack.my_pop()
        if k == 0:
            break

    ans = ""
    for i in range(n):
        if i in dic:
            ans += s[i]

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，给定规模 n
    main(10)