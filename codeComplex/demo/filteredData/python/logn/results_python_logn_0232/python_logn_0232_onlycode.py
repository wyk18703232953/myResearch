n, s = input().split()

n = int(n)
s = int(s)


def get_decimal_value_digits(number):
    count = 0
    digits = 0
    number = str(number)
    for digit in number:
        count += int(digit)
        digits += 1
    return count


def is_big_num(number, s):
    if (number - get_decimal_value_digits(number)) >= s:
        return True
    return False


start = s
end = n
count = 0
digits = 0
half = (n + s) // 2

while (end - start) >= 0:
    half = (start + end) // 2
    #decimal = get_decimal_value_digits(half)
    # if is big number
    if is_big_num(half, s):
        end = half - 1
    else:
        start = half + 1

if not is_big_num(start+1, s):
    print(0)
else:
    print(n - start + 1)
		 			 	 		 	 		 		   		   	  	