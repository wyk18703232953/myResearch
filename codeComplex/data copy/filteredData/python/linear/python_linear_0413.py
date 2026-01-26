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

def core_logic(n, k, kk):
    if k > 13:
        return -1
    dic = {}
    for index, value in enumerate("abcdefghijklmnopqrstuvwxyz"):
        dic[value] = index + 1
    s = sorted(list(set(kk)))
    if not s:
        return -1
    ans = 0
    ans += dic[s[0]]
    k -= 1
    curr = s[0]
    for i in range(1, len(s)):
        if k:
            if dic[s[i]] > dic[curr] + 1:
                ans += dic[s[i]]
                curr = s[i]
                k -= 1
            if k == 0:
                break
    if k == 0:
        return ans

    else:
        return -1

def main(n):
    # n controls string length, k is derived deterministically from n
    if n <= 0:
        n = 1
    k = (n % 15) + 1
    base = "abcdefghijklmnopqrstuvwxyz"
    kk = [base[i % 26] for i in range(n)]
    res = core_logic(n, k, kk)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)