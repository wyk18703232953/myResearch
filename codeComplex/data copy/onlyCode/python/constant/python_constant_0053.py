import itertools

def q121a_v2():
	good_num_arr = generate_47_arr()
	num = int(input())
	for element in good_num_arr:
		if(num % element == 0):
			print("YES")
			return
	print("NO")


def generate_47_arr():
	arr = []
	for digits in range(1, 4):
		arr += itertools.product("47", repeat=digits)
	for i in range(len(arr)):
		arr[i] = int("".join(list(arr[i])))
	arr.append(4444444444)
	return arr

q121a_v2()