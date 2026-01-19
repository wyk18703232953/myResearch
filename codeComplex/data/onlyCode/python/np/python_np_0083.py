from math import factorial
def C(m,n):
    return factorial(n) // (factorial(m) * factorial(n - m))

command_1, command_2 = input(), input()
num = command_2.count('?')
i = command_1.count('+') - command_1.count('-') -\
command_2.count('+') + command_2.count('-') + num
if i % 2 == 0 and 0 <= i//2 <= num:
    print("%.9f"%(C(i//2, num) / 2**num))
else:
    print("0.000000000")