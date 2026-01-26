def main():
	l, r = map(int , input().split())
	if l == r :
		print(0)
	else :
		rs = ""
		while (r):
			rs += '1' if r%2 else '0'
			r //= 2
		for i in range(len(rs), 65):
			rs += '0' 
		# rs = rs[::-1]
		ls = ""
		while (l):
			ls += '1' if l%2 else '0'
			l //= 2
		for i in range(len(ls), 65):
			ls += '0'
		# ls = ls[::-1]
		pos = -1
		for i in range(64, -1, -1):
			# print(rs[i], '#', ls[i])
			if (rs[i] == '1' and ls[i] == '0'):
				pos = i
				break

		ans = 2**(pos+1) - 1
		print(ans)

if __name__ == '__main__':
	main()