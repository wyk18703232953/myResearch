def factors(n):    
    from functools import reduce
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

import math

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

def core_algorithm(n, k, s):
    arrStack = My_stack()
    dic={}
    for i in range(n):
        if s[i]=="(":
            arrStack.my_push([i,"("])

        else:
            if not arrStack.isEmpty() and arrStack.my_peak()[1]=="(":
                index=arrStack.my_peak()[0]
                dic[index]=1
                dic[i]=1
                k-=2
                arrStack.my_pop()
        if k==0:
            break
    ans =""
    for i in range(n):
        if i in dic:
            ans+=s[i]
    return ans

def generate_input(n):
    if n < 2:
        n = 2
    if n % 2 == 1:
        n += 1
    k = n
    pattern = "()"
    s = []
    for i in range(n):
        s.append(pattern[i % 2])
    return n, k, s

def main(n):
    n_gen, k, s = generate_input(n)
    result = core_algorithm(n_gen, k, s)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)