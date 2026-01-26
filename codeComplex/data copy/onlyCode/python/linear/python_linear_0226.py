_ = int(input())
binary_number = input()

if binary_number == '0':
    print('0')
else:
    count_0 = sum(1 for b in binary_number if b == '0')
    count_1 = sum(1 for b in binary_number if b == '1')
    print('1' + '0' * count_0)
