from collections import deque as de
import math
from collections import Counter as cnt

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

def get_frequency(list_):
    dic = {}
    for ele in list_:
        if ele in dic:
            dic[ele] += 1
        else:
            dic[ele] = 1
    return dic

def main(n):
    sizes = ["M", "S", "L", "XL", "XXL", "XXXL", "XS", "XXS", "XXXS"]
    pl = [sizes[i % len(sizes)] for i in range(n)]
    nl = [sizes[(i * 2 + 3) % len(sizes)] for i in range(n)]

    ans = 0
    pmc = pl.count("M")
    mc = nl.count("M")
    if pmc < mc:
        ans += mc - pmc

    psc = pl.count("S")
    sc = nl.count("S")
    if psc < sc:
        ans += sc - psc

    plc = pl.count("L")
    lc = nl.count("L")
    if plc < lc:
        ans += lc - plc

    pxlc = pl.count("XL")
    xlc = nl.count("XL")
    if pxlc < xlc:
        ans += xlc - pxlc

    pxxlc = pl.count("XXL")
    xxlc = nl.count("XXL")
    if pxxlc < xxlc:
        ans += xxlc - pxxlc

    pxxxlc = pl.count("XXXL")
    xxxlc = nl.count("XXXL")
    if pxxxlc < xxxlc:
        ans += xxxlc - pxxxlc

    pxsc = pl.count("XS")
    xsc = nl.count("XS")
    if pxsc < xsc:
        ans += xsc - pxsc

    pxxsc = pl.count("XXS")
    xxsc = nl.count("XXS")
    if pxxsc < xxsc:
        ans += xxsc - pxxsc

    pxxxsc = pl.count("XXXS")
    xxxsc = nl.count("XXXS")
    if pxxxsc < xxxsc:
        ans += xxxsc - pxxxsc

    print(ans)

if __name__ == "__main__":
    main(10)