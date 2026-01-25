def solve(n, arr):
	s = sum(arr)
	if s == 0:
		return "cslnb"

	n_num = {}

	for item in arr:
		if item in n_num:
			n_num[item] += 1
		else:
			n_num[item] = 1

	if 0 in n_num and n_num[0] >= 2:
		return 'cslnb'

	for key in n_num.keys():
		if n_num[key] >= 3:
			return "cslnb"

	ind_pairs = []
	for key in n_num.keys():
		if n_num[key] == 2:
			ind_pairs.append(key)

	if len(ind_pairs) >= 2:
		return "cslnb"
	elif len(ind_pairs) == 1 and (ind_pairs[0]-1) in n_num:
		return "cslnb"
	else:
		sum_targ = n*(n-1) // 2
		dif_sum = s - sum_targ
		if dif_sum % 2 == 0:
			return "cslnb"
		else:
			return "sjfnb"


def main(n):
	# 确定性构造：数组长度为 n，第 i 个元素为 i//2
	# 这样同一 n 多次运行始终一致
	arr = [i // 2 for i in range(n)]
	result = solve(n, arr)
	print(result)


if __name__ == "__main__":
	# 示例调用，可根据需要修改 n 进行实验
	main(10)