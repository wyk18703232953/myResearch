n = int(input())
a = iter(map(int, input().split()))
prev_type = 3
prev_res = 2
curr_a = next(a)
res = []
for _ in range(1):
	for next_a in a:
		if next_a > curr_a:
			if prev_type == 1 or prev_res == 1:
				prev_res += 1
				if prev_res == 5:
					break
			else:
				prev_res = 1
			prev_type = 1
		elif next_a < curr_a:
			if prev_type == 2 or prev_res == 5:
				prev_res -= 1
				if prev_res == 1:
					break
			else:
				prev_res = 5
			prev_type = 2
		else:
			if prev_type == 1:
				prev_res += 1
			elif prev_type == 2:
				prev_res -= 1
			elif prev_res != 2:
				prev_res = 2
			else:
				prev_res = 3
			prev_type = 3
		res.append(prev_res)
		curr_a = next_a
	else:
		if prev_type == 1:
			res.append(prev_res + 1)
		elif prev_type == 2:
			res.append(prev_res - 1)
		elif prev_res != 1:
			res.append(1)
		else:
			res.append(2)
		print(*res)
		break
else:
	print('-1')
