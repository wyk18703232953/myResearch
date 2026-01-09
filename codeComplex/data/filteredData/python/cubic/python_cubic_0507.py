def main(n):
	N = n
	M = n
	K = 2 * n  # even, scales with n

	R = range
	m = min

	# If K is odd (here it's always even), output -1 matrix for correctness preservation
	if K & 1:
		for _ in R(N):
			# print(*([-1] * M))
			pass
		return

	# Deterministic generation of A (N x (M-1)) and B ((N-1) x M)
	# A[i][j] = (i + j) % 7 + 1
	# B[i][j] = (i * 2 + j * 3) % 9 + 1
	A = [[(i + j) % 7 + 1 for j in R(M - 1)] for i in R(N)]
	B = [[(i * 2 + j * 3) % 9 + 1 for j in R(M)] for i in R(N - 1)]

	X = [[0] * M for _ in R(N)]

	for _k in R(1, K // 2 + 1):
		Y = [[9 ** 9] * M for _ in R(N)]
		for i in R(N):
			for j in R(M):
				if i:
					Y[i][j] = X[i - 1][j] + 2 * B[i - 1][j]
				if i < N - 1:
					Y[i][j] = m(Y[i][j], X[i + 1][j] + 2 * B[i][j])
				if j:
					Y[i][j] = m(Y[i][j], X[i][j - 1] + 2 * A[i][j - 1])
				if j < M - 1:
					Y[i][j] = m(Y[i][j], X[i][j + 1] + 2 * A[i][j])
		X = Y

	for x in X:
		# print(*x)
		pass
if __name__ == "__main__":
	main(5)