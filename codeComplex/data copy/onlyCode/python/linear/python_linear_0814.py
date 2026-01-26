n = int(input())

arr = list(map(int, input().split()))

solved = False
s = sum(arr)
if s == 0:
	print("cslnb")
	solved = True

if not solved:
	n_num = {}

	for item in arr:
		if item in n_num:
			n_num[item] += 1
		else:
			n_num[item] = 1

	if 0 in n_num and n_num[0] >= 2:
		print('cslnb')
		solved = True

	if not solved:
		for key in n_num.keys():
			if n_num[key] >= 3:
				print("cslnb")
				solved = True

		ind_pairs = []
		if not solved:
			for key in n_num.keys():
				if n_num[key] == 2:
					ind_pairs.append(key)

			if len(ind_pairs) >= 2:
				print("cslnb")
				solved = True
			elif len(ind_pairs) == 1 and (ind_pairs[0]-1) in n_num:
				print("cslnb")
				solved = True
			else:
				# print('s', s)
				sum_targ = n*(n-1) // 2
				# print('sum_targ', sum_targ)
				dif_sum = s - sum_targ
				# print("dif_sum", dif_sum)
				if dif_sum % 2 == 0:
					print("cslnb")
				else:
					print("sjfnb")