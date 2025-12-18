# A. Minimum Binary Number

n = int(input())
s = input()

if n == 1:
    print(s)
else:
    zeros = s.count('0')
    print('1' + zeros * '0')
