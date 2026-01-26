import math
n = int(input())
A = [i + 1 for i in range(n)]
x = int(math.sqrt(n))
X = [A[i:i + x] for i in range(0, len(A), x)]
X = X[::-1]
f = [item for sublist in X for item in sublist]
print(*f)