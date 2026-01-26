n = int(input())
s = input()
x = s.count('0')
if s == '0':
    print('0')
else:
    print('1' + '0'*x)