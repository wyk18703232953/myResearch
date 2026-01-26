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
    import math
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
    return (math.log10(x) / 
            math.log10(2)); 

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
    return (math.ceil(Log2(n)) == math.floor(Log2(n))); 

def checkisap(list_):
    d=list_[1]-list_[0]
    for i in range(2,len(list_)):
        temp=list_[i]-list_[i-1]
        if temp !=d:
            return False
    return True

def ceildiv(x,y): 
    return (x+y-1)//y 

def core_logic(n, pos, l, r):
    if l==1 and r==n:
        return 0

    else:
        if pos < l:
            ans=l-pos+1
            if r <n:
                ans+=(r-l)
                ans+=1
            return ans
        elif l<=pos<=r:
            if l >1 and r<n:
                ans=(r-l)
                ans+=min(pos-l,r-pos)
                ans+=2
            elif l>1 and r==n:
                ans=pos-l
                ans+=1

            else:
                ans=r-pos
                ans+=1
            return ans

        else:
            ans=pos-r+1
            if l>1:
                ans+=(r-l)
                ans+=1
            return ans

def generate_input(n):
    # n controls the scale: we create parameters of order n
    # Ensure n is at least 4 for meaningful intervals
    if n < 4:
        n_eff = 4

    else:
        n_eff = n
    # Define interval [l, r] within [1, n_eff]
    # Make it deterministic based on n_eff
    l = (n_eff // 4) + 1
    r = (3 * n_eff) // 4
    if l < 1:
        l = 1
    if r > n_eff:
        r = n_eff
    if l > r:
        l, r = 1, n_eff
    # Position pos: place it deterministically
    # Cycle through three regimes as n changes to exercise all branches
    mode = n_eff % 3
    if mode == 0:
        # pos < l
        pos = max(1, l-1)
    elif mode == 1:
        # l <= pos <= r
        pos = (l + r) // 2

    else:
        # pos > r
        pos = min(n_eff, r+1)
    return n_eff, pos, l, r

def main(n):
    n_param, pos, l, r = generate_input(n)
    ans = core_logic(n_param, pos, l, r)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)