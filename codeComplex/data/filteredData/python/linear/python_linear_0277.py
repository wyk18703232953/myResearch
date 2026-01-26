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

def get_frequency(list_):
    dic={}
    for ele in list_:
        if ele in dic:
            dic[ele] += 1

        else:
            dic[ele] = 1
    return dic

def Log2(x): 
    import math
    return (math.log10(x) / math.log10(2))

def isPowerOfTwo(n): 
    import math
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

def core_logic(n, m, a, b):
    if n % m:
        ul = (n // m) + 1
        ll = n // m
        return min(((ul * m) - n) * a, (n - (ll * m)) * b)

    else:
        return 0

def main(n):
    # Input structure: single test case with four integers n, m, a, b.
    # We map the external scale `n` to these as:
    # N = n, M = max(1, n//2), A = n+1, B = n+2 for n>0.
    # For n==0, use fixed small values but keep determinism.
    if n <= 0:
        N = 1
        M = 1
        A = 1
        B = 1

    else:
        N = n
        M = max(1, n // 2)
        A = n + 1
        B = n + 2
    result = core_logic(N, M, A, B)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call; change the argument to test other scales.
    main(10)