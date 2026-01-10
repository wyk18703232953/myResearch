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

arrStack = My_stack() 

def decimalToBinary(n): 
    return bin(n).replace("0b", "")

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
    import math
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
    dic={}
    for ele in lst:
        if ele in dic:
            dic[ele] += 1
        else:
            dic[ele] = 1
    return dic

def Log2(x): 
    import math
    return (math.log10(x) / math.log10(2))

def getProduct(n):
    product = 1
    while (n != 0):
        product = product * (n % 10)
        n = n // 10
    return product

def lcm(x,y):
    import math
    lcm_val = (x*y)//math.gcd(x,y)
    return lcm_val

def isPowerOfTwo(n): 
    import math
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

def checkisap(lst):
    d=lst[1]-lst[0]
    for i in range(2,len(lst)):
        temp=lst[i]-lst[i-1]
        if temp !=d:
            return False
    return True

def primes_method5(n):
    out ={}
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out[p]=1
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

def getSum(n): 
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)

def ceildiv(x,y): 
    return (x+y-1)//y 

def main(n):
    if n <= 0:
        return
    a = list(range(1, n+1))
    a.sort()
    if a[n-1]==1:
        a[n-1]=2
    else:
        a[n-1]=1
    a.sort()
    print(*a)

if __name__ == "__main__":
    main(10)