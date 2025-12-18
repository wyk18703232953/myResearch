lst = list()

lst.append(0)
lst.append(1)

now = 1
while now <= 1e25 :
	now = now * 4 + 1
	# print(now)
	lst.append(now)

t = int(input())

for i in range(t):
	s = input().split()
	n = int(s[0])
	k = int(s[1])
	if(n >= 34):
		print("YES " + str(n - 1))
		continue

	sek = 0
	ambil = 1
	nyak = 0
	cnt = 0

	sudah = False
	while (sek < n):
		cnt = cnt + (1 << (sek + 1)) - 1
		# print(str(cnt) + " here")
		if cnt > k:
			print("NO")
			sudah = True
			break

		next_ambil = (ambil + 1) * 2 - 1
		sisa = 4 * ambil - next_ambil
		ambil = next_ambil

		sek += 1
		nyak = nyak + sisa * lst[n - sek]
		if (nyak + cnt) >= k :
			print("YES " + str(n - sek))
			sudah = True
			break

	if sudah == False:
		print("NO")
