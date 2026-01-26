import math
def islucky(x):
    digits = set(list(str(x)))
    return (len(digits) == 2 and ("4" in digits and "7" in digits)) or (len(digits) == 1 and ("4" in digits or "7" in digits))
a = int(input())
lucky = islucky(a)
for i in range(2, math.ceil(math.sqrt(a))+1):
    if a % i == 0:
        #print(i, a / i)
        if islucky(i) or islucky(a // i):
            lucky = True
            break

print("YES" if lucky else "NO")