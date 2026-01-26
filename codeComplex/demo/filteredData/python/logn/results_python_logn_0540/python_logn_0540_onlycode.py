k = int(input())

if k <= 9:
	print(k)

else:
	s = 9
	n = 1
	
	while s < k:
		n += 1
		prev_s = s
		s += (10**n - 10**(n-1)) * n

	digit_pos = k - (prev_s + 1)
	number = 10**(n-1) + digit_pos // n
	
	if digit_pos / n != digit_pos // n:
		digit_pos = digit_pos - (digit_pos // n) * n


	else:
		digit_pos = 0

	print(str(number)[digit_pos])