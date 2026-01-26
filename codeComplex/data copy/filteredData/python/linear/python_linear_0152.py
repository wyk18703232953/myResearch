import math
from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))

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
        return len(self.data) == 0

arrStack = My_stack()

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def binarytodecimal(n):
    return int(n, 2)

def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
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

def get_frequency(list_):
    dic = {}
    for ele in list_:
        if ele in dic:
            dic[ele] += 1

        else:
            dic[ele] = 1
    return dic

def Log2(x):
    return (math.log10(x) /
            math.log10(2))

def getProduct(n):
    product = 1
    while (n != 0):
        product = product * (n % 10)
        n = n // 10
    return product

def dupconscount(nums):
    element = []
    freque = []
    if not nums:
        return element
    running_count = 1
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            running_count += 1

        else:
            freque.append(running_count)
            element.append(nums[i])
            running_count = 1
    freque.append(running_count)
    element.append(nums[i + 1])
    return element, freque

def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

def ceildiv(x, y):
    return (x + y - 1) // y

def main(n):
    # 输入结构：
    # 原程序：n, p 然后长度为 n 的数组 a
    # 这里将规模参数 n 直接作为原来的 n
    if n <= 0:
        # print(0)
        pass
        return
    p = n + 1
    a = [i + 1 for i in range(n)]
    fir = a[0]
    sec = sum(a) - fir
    ans = (fir % p) + (sec % p)
    for i in range(1, n):
        fir += a[i]
        sec -= a[i]
        temp = (fir % p) + (sec % p)
        if temp > ans:
            ans = temp
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)