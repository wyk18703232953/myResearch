#!usr/bin/python

a = input()
b = input()

length_of_a = len(a)
length_of_b = len(b)
found_digit = False
chk_finnish = False
appended_digit_count = 0
n = {}
num = []
for i in range(0,10):
	n[i] = 0

for i in range(0,length_of_a):
	c = int(a[i])
	n[c] += 1


if length_of_a < length_of_b:
	num = sorted(a,reverse=True)
	for i in range(0,length_of_a):
		print(num[i],end="")
else:
	for i in range(0,length_of_b):
		digit = int(b[i])
		if n[digit] > 0:
			num.append(digit)
			n[digit] -= 1
			# print("from start as equal : n["+str(digit)+"] : "+str(n[digit]))
			# print(num)
			appended_digit_count += 1
		else:
			j = digit - 1
			while j > -1:
				if n[j] > 0:
					num.append(j)
					appended_digit_count += 1
					n[j] -= 1
					# print("from 2nd : n["+str(j)+"] : "+str(n[j]))
					# print(num)
					found_digit = True
					chk_finnish = True
					break
				j -= 1

			if found_digit:
				j = 9
				while j > -1:
					if n[j] > 0:
						digit_count = n[j]
						for k in range(0,digit_count):
							num.append(j)
							n[j] -= 1
							# print("form 3rd : n["+str(j)+"] : "+str(n[j]))
							# print(num)
							appended_digit_count += 1
					j -= 1
				if chk_finnish:
					break
			else:
				found_digit = False
				while found_digit == False:
					pop_up = num[appended_digit_count-1]
					# print(pop_up,end=" ")
					del num[-1]
					j = pop_up - 1
					n[pop_up] += 1
					# print("form 4th popped : n["+str(pop_up)+"] : "+str(n[pop_up]))
					# print(num)
					# print(n[pop_up])
					appended_digit_count -= 1
					while j > -1:
						if n[j] > 0:
							num.append(j)
							appended_digit_count += 1
							n[j] -= 1
							# print("from 5th appeneded n["+str(j)+"] : "+str(n[j]))
							# print(num)
							found_digit = True
							break
						j -= 1
				j = 9
				while j > -1:
					if n[j] > 0:
						# print("from 5th : n["+str(j)+"] : "+str(n[j]))
						# print(num)
						digit_count = n[j]
						for k in range(0,digit_count):
							num.append(j)
							appended_digit_count += 1
					j -= 1
				break
			

	for i in range(0,length_of_b):
		print(num[i],end="")