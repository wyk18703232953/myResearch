def mergeSort(x):
	if len(x) > 1:
		mid = len(x)//2
		L = x[:mid]
		R = x[mid:]
		mergeSort(L)
		mergeSort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] > R[j]:
				x[k] = L[i]
				i += 1
			else:
				x[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			x[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			x[k] = R[j]
			j += 1
			k += 1

def core_logic(n, m, pairs):
	difference = []
	total = 0
	for a, b in pairs:
		total += a
		difference.append(a - b)
	mergeSort(difference)
	minimum = 0
	if total <= m:
		return 0
	else:
		for val in difference:
			minimum += 1
			total = total - val
			if total <= m:
				break
		if total > m:
			return -1
		else:
			return minimum

def main(n):
	# n: number of (a, b) pairs
	# Deterministic generation of n, m, and pairs
	if n <= 0:
		n = 1
	# Let m be about half of the sum of a's for determinism
	# Generate a and b deterministically
	pairs = []
	total_a = 0
	for i in range(1, n + 1):
		a = (i * 3) % (2 * n + 1) + 1
		b = (i * 5) % (2 * n + 1)
		pairs.append((a, b))
		total_a += a
	# Set m to be a deterministic function of total_a
	m = total_a // 2
	result = core_logic(n, m, pairs)
	print(result)

if __name__ == "__main__":
	main(10)