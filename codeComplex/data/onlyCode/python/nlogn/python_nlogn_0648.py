from math import *
import sys

input = sys.stdin.readline



def bin_search(arr, n):

	pos = -1

	# all nums < n

	for i in range(35, -1, -1):
		jump = (1 << i)

		if (pos + jump) >= len(arr):
			continue

		if arr[pos + jump] <= n-1:
			pos += jump


	return len(arr) - pos - 1  

def main():
	n, m = [int(x) for x in input().split(' ')]

	vert = []
	for i in range(n):
		vert.append(int(input()))

	hor = []
	for i in range(m):
		col1, col2, row = [int(x) for x in input().split(' ')]

		if col1 != 1:
			continue

		hor.append((col2))


	vert.append(1000000000)

	vert = sorted(vert)
	hor = sorted(hor)

	best = int(1e10)


	for i in range(len(vert)):
		cur_ans = bin_search(hor, vert[i]) + i
		best = min(best, cur_ans)



	print(best)

if __name__ == "__main__":
	main()