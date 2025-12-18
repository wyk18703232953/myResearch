import sys,math

def read_int():
	return int(sys.stdin.readline().strip())

def read_int_list():
	return list(map(int,sys.stdin.readline().strip().split()))

def read_string():
	return sys.stdin.readline().strip()

def read_string_list(delim=" "):
	return sys.stdin.readline().strip().split(delim)


###### Author : Samir Vyas #######
###### Write Code Below    #######
k = read_int()

base_digit_number = 1; expo = 0

while k >= base_digit_number:
	base_digit_number += 9*(expo+1)*(10**expo)
	expo += 1

base_digit_number -= 9*(expo)*(10**(expo-1))

ans_number = (k - base_digit_number)//expo + 10**(expo-1)

ans_digit = str(ans_number)[(k - base_digit_number)%expo]

print(ans_digit)
