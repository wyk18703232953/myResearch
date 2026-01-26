n = input()
s = input()
n = int(n)
print('1'*min(s.count('1'), 1)+'0'*s.count('0'))