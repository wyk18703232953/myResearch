n, k = list(map(int,input().split()))
chuj_twojej_starej = (n - k) // 2 + 1
i = 1
while True:
	if i % chuj_twojej_starej == 0:
		print(0, end = "")
	else:
		print(1, end = "")
	if i == n:
		break
	i += 1