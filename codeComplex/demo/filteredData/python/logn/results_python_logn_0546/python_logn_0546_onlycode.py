k = int(input())

total_digit = 0
digit = 1

while k > total_digit + digit * (pow(10, digit) - pow(10, digit - 1)):
    total_digit += digit * (pow(10, digit) - pow(10, digit - 1))
    digit += 1

remaining = k - total_digit - 1
corr_num = str(pow(10, digit - 1) + remaining // digit)
print(corr_num[remaining % digit])
